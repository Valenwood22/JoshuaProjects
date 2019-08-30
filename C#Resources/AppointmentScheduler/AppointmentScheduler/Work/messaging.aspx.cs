using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AppointmentScheduler.Work
{
    public partial class advising : System.Web.UI.Page
    {

        public void Refresh()
        {
            SqlConnection conn = new SqlConnection("Data Source=(LocalDB)\\MSSQLLocalDB;AttachDbFilename=|DataDirectory|ProjectDB.mdf;Integrated Security=True;Connect Timeout=30");
            conn.Open();
            conn.Close();

        }

        protected void Page_Load(object sender, EventArgs e)
        {
            
        }

        protected void GridView1_SelectedIndexChanged(object sender, EventArgs e)
        {

            SqlConnection conn = new SqlConnection("Data Source=(LocalDB)\\MSSQLLocalDB;AttachDbFilename=|DataDirectory|ProjectDB.mdf;Integrated Security=True;Connect Timeout=30");
            conn.Open();

            int I = GridView1.SelectedRow.RowIndex;
            var localTime = GridView1.Rows[I].Cells[1].Text;
  
            string selstr = "select MSGText from MSGTable where MSGDate = @time"; //
            SqlCommand cmd = new SqlCommand(selstr, conn);
            SqlParameter time = cmd.Parameters.Add("@time", SqlDbType.DateTime);
            time.Value = localTime;

            SqlDataReader rdr = cmd.ExecuteReader();

            if (rdr.Read())
            {
                TextBox1.Text = rdr.GetValue(0).ToString();
            }
            else
            {
                Console.WriteLine("not available yet");
            }



            conn.Close();
        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            string msgto = TextBox2.Text;
            string msgbody = TextBox1.Text;

            SqlConnection conn = new SqlConnection("Data Source=(LocalDB)\\MSSQLLocalDB;AttachDbFilename=|DataDirectory|ProjectDB.mdf;Integrated Security=True;Connect Timeout=30");
            conn.Open();

            string selstr = "INSERT INTO MSGTable(FromEmail,TOEmail,MSGText,MSGDate,MSGTime)" +
                "VALUES(@from,@to,@text,@date,@time)";
            SqlCommand cmd = new SqlCommand(selstr, conn);

            SqlParameter Afrom = cmd.Parameters.Add("@from", SqlDbType.VarChar, 50);
            Afrom.Value = Logon.UserName;

            SqlParameter Ato = cmd.Parameters.Add("@to", SqlDbType.VarChar, 50);
            Ato.Value = msgto;

            SqlParameter Atext = cmd.Parameters.Add("@text", SqlDbType.VarChar, 50);
            Atext.Value = msgbody;

            string tod = (DateTime.Today.Date + DateTime.Now.TimeOfDay).ToString();
            SqlParameter date = cmd.Parameters.Add("@date", SqlDbType.DateTime);
            date.Value = tod;

            SqlParameter time = cmd.Parameters.Add("@time", SqlDbType.Time, 7);
            time.Value = DateTime.Now.TimeOfDay;

            SqlDataReader rdr = cmd.ExecuteReader();

            rdr.Close();

            SqlDataSource1.EnableCaching = false;
            GridView1.DataBind();
            SqlDataSource1.EnableCaching = true;

            TextBox1.Text = "";
            TextBox2.Text = "";

        }

        protected void TextBox1_TextChanged(object sender, EventArgs e)
        {
            
        }

        protected void SqlDataSource1_Selecting(object sender, System.Web.UI.WebControls.SqlDataSourceSelectingEventArgs e)
        {

        }

        protected void ListView1_SelectedIndexChanged(object sender, EventArgs e)
        {
         
        }

        protected void TextBox1_TextChanged1(object sender, EventArgs e)
        {

        }

        protected void TextBox1_TextChanged2(object sender, EventArgs e)
        {

        }

        protected void Button2_Click(object sender, EventArgs e)
        {

        }

    }
}
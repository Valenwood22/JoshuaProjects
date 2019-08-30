using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Windows;

namespace AppointmentScheduler.Work
{
    public partial class messaging : System.Web.UI.Page
    {
        public static int AdvisorID = -1;
        public static int StudentID = -1;
        public static string OutputName = "";
        
       


        public void Refresh()
        {
            SqlConnection conn = new SqlConnection("Data Source=(LocalDB)\\MSSQLLocalDB;AttachDbFilename=|DataDirectory|ProjectDB.mdf;Integrated Security=True;Connect Timeout=30");
            conn.Open();
            conn.Close();

        }


        protected void Page_Load(object sender, EventArgs e)
        {


            if (Logon.UserRole.Equals("Student"))
            {
                Label1.Text = "Advisor Information:";
                SqlConnection conn = new SqlConnection("Data Source=(LocalDB)\\MSSQLLocalDB;AttachDbFilename=|DataDirectory|ProjectDB.mdf;Integrated Security=True;Connect Timeout=30");
                conn.Open();


                string selstr = "select StudentAdvisorID,StudentID,StudentLastName,StudentFirstName from StudentTable where StudentUserName = @name"; //
                SqlCommand cmd = new SqlCommand(selstr, conn);
                SqlParameter name = cmd.Parameters.Add("@name", SqlDbType.VarChar, 50);
                name.Value = Logon.UserName;
                SqlDataReader rdr = cmd.ExecuteReader(); ;

                if (rdr.Read())
                {
                    AdvisorID = Int32.Parse(rdr.GetValue(0).ToString());
                    StudentID = Int32.Parse(rdr.GetValue(1).ToString());
                    OutputName = rdr.GetValue(2).ToString() + ", " + rdr.GetValue(3).ToString();
                }
                rdr.Close();
                Session.Add("AdvisorID", AdvisorID);


                string selstr2 = "Select AdvisorFirstName, AdvisorLastName, AdvisorLocation from AdvisorTable where AdvisorID = @id";
                SqlCommand cmd2 = new SqlCommand(selstr2, conn);
                SqlParameter id = cmd2.Parameters.Add("@id", SqlDbType.Int);
                id.Value = AdvisorID;
                SqlDataReader rdr2 = cmd2.ExecuteReader();

                if (rdr2.Read())
                {
                    
                    DropDownList1.Items.Add(rdr2.GetSqlValue(0).ToString() + "  " + rdr2.GetSqlValue(1).ToString() + "  "+ rdr2.GetSqlValue(2).ToString());
                }
                else
                {
                    DropDownList1.Items.Add("Not Logged In");
                    // TextBox1.Text = "Not Logged In";
                }



                conn.Close();
            }
            else if (Logon.UserRole.Equals("Advisor"))
            {
                Label1.Text = "Student Information:";
                SqlConnection conn = new SqlConnection("Data Source=(LocalDB)\\MSSQLLocalDB;AttachDbFilename=|DataDirectory|ProjectDB.mdf;Integrated Security=True;Connect Timeout=30");
                conn.Open();

                string selstr2 = "Select AdvisorID from AdvisorTable where AdvisorUserName = @name";
                SqlCommand cmd2 = new SqlCommand(selstr2, conn);
                SqlParameter name = cmd2.Parameters.Add("@name", SqlDbType.VarChar, 50);
                name.Value = Logon.UserName;
                SqlDataReader rdr2 = cmd2.ExecuteReader();



                if (rdr2.Read())
                {
                    string SAdvisorID = rdr2.GetSqlValue(0).ToString();
                    AdvisorID = Int32.Parse(SAdvisorID);
                }
                else
                {
                   // TextBox1.Text = "Not Logged In";
                }
               rdr2.Close();




                string selstr = "select StudentFirstName,StudentLastName from StudentTable where StudentAdvisorID = @Aid"; //
                SqlCommand cmd = new SqlCommand(selstr, conn);
                SqlParameter Aid = cmd.Parameters.Add("@Aid", SqlDbType.Int);
                Aid.Value = AdvisorID;
                SqlDataReader rdr = cmd.ExecuteReader();


                //if (rdr.Read())
                // {
                    DropDownList1.Items.Add("");
                    var List = new List<String>();
                    while (rdr.Read())
                    {
                        List.Add(rdr.GetSqlValue(0).ToString() + "  " + rdr.GetSqlValue(1).ToString());
                    }
                    foreach (string x in List)
                    {
                        DropDownList1.Items.Add(x);
                    }
               // }



                
                conn.Close();
            }
            else
                DropDownList1.Items.Add("Not Logged In");
                //TextBox1.Text = "Invalid login";
        }

        protected void Button1_Click(object sender, EventArgs e)
        {

            SqlConnection conn = new SqlConnection("Data Source=(LocalDB)\\MSSQLLocalDB;AttachDbFilename=|DataDirectory|ProjectDB.mdf;Integrated Security=True;Connect Timeout=30");
            conn.Open();

            int index = GridView1.SelectedRow.RowIndex;
            int Aid = Int32.Parse(GridView1.Rows[index].Cells[3].Text);
            
            string selstr = "DELETE FROM AppointmentTable WHERE AppointmentID=@idx";
            SqlCommand cmd = new SqlCommand(selstr, conn);
            SqlParameter idx = cmd.Parameters.Add("@idx", SqlDbType.Int);
            idx.Value = Aid;
            SqlDataReader rdr = cmd.ExecuteReader();
            
            rdr.Close();
            
            SqlDataSource2.EnableCaching = false;
            GridView1.DataBind();
            SqlDataSource2.EnableCaching = true;
            
        }

        protected void Button2_Click(object sender, EventArgs e)
        {
            
            string time = TextBox4.Text;
            string reason = TextBox3.Text;
            string date = TextBox2.Text+" "+time;
            int StID = 0;

            SqlConnection conn = new SqlConnection("Data Source=(LocalDB)\\MSSQLLocalDB;AttachDbFilename=|DataDirectory|ProjectDB.mdf;Integrated Security=True;Connect Timeout=30");
            conn.Open();

            string selstr = "INSERT INTO AppointmentTable(AppointmentTime,AppointmentDate,AppointmentReason,AdvisorID,StudentID)" +
                "VALUES(@time,@date,@reason,@AID,@SID)";
            SqlCommand cmd = new SqlCommand(selstr, conn);

            SqlParameter Atime = cmd.Parameters.Add("@time", SqlDbType.Time, 7);
            Atime.Value = time;

            SqlParameter Adate = cmd.Parameters.Add("@date", SqlDbType.DateTime);
            Adate.Value = date;

            SqlParameter Areason = cmd.Parameters.Add("@reason", SqlDbType.VarChar, 50);
            Areason.Value = reason;

            SqlParameter AID = cmd.Parameters.Add("@AID", SqlDbType.Int);
            AID.Value = AdvisorID;

            SqlParameter SID = cmd.Parameters.Add("@SID", SqlDbType.Int);
            SID.Value = StudentID;

            SqlDataReader rdr = cmd.ExecuteReader();

            rdr.Close();

            SqlDataSource2.EnableCaching = false;
            GridView1.DataBind();
            SqlDataSource2.EnableCaching = true;

            MessageBox.Show("Appointment Scheduled.\n" + date + " " + reason + "\n" + OutputName);

            TextBox2.Text = "";
            TextBox3.Text = "";
            TextBox4.Text = "";

        }

        protected void TextBox3_TextChanged(object sender, EventArgs e)
        {

        }

        protected void GridView1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        protected void DropDownList1_SelectedIndexChanged(object sender, EventArgs e)
        {
            SqlConnection conn = new SqlConnection("Data Source=(LocalDB)\\MSSQLLocalDB;AttachDbFilename=|DataDirectory|ProjectDB.mdf;Integrated Security=True;Connect Timeout=30");
            conn.Open();


            string selstr = "select StudentID from StudentTable where StudentFirstName = @name"; //
            SqlCommand cmd = new SqlCommand(selstr, conn);
            SqlParameter name = cmd.Parameters.Add("@name", SqlDbType.VarChar, 50);
            string[] tempName = DropDownList1.SelectedValue.Split(' ');
            name.Value = tempName[0];
            SqlDataReader rdr = cmd.ExecuteReader();
            OutputName = DropDownList1.SelectedValue;

            if (rdr.Read())
            {
                StudentID = Int32.Parse(rdr.GetSqlValue(0).ToString());
            }
            rdr.Close();
        }
    }
}
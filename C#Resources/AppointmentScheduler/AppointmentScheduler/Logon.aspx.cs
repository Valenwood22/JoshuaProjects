using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Web.Security;
using System.Data.Entity;
using System.Data.SqlClient;
using System.Data;

namespace AppointmentScheduler
{
    

    public partial class Logon : System.Web.UI.Page
    {
        public static string UserName = "";
        public static string StudentID = "";
        public static string UserRole = "";

        public void Refresh()
        {
            SqlConnection conn = new SqlConnection("Data Source=(LocalDB)\\MSSQLLocalDB;AttachDbFilename=|DataDirectory|ProjectDB.mdf;Integrated Security=True;Connect Timeout=30");
            conn.Open();
            conn.Close();

        }


        protected void Page_Load(object sender, EventArgs e)
        {
            UnobtrusiveValidationMode = System.Web.UI.UnobtrusiveValidationMode.None;

        }

        protected void Login1_Authenticate(object sender, AuthenticateEventArgs e)
        {
            SqlConnection conn = new SqlConnection("Data Source=(LocalDB)\\MSSQLLocalDB;AttachDbFilename=|DataDirectory|ProjectDB.mdf;Integrated Security=True;Connect Timeout=30");
            conn.Open();

            string selstr = "select UserName, UserRole from UserTable where UserName = @name AND UserPassword = @pswrd"; //
            SqlCommand cmd = new SqlCommand(selstr, conn);
            SqlParameter name = cmd.Parameters.Add("@name", SqlDbType.VarChar, 50);
            SqlParameter pswrd = cmd.Parameters.Add("@pswrd", SqlDbType.VarChar, 50);
            name.Value = Login1.UserName.ToString();
            pswrd.Value = Login1.Password.ToString();

            SqlDataReader rdr = cmd.ExecuteReader();
            if (rdr.Read())
            {
                UserName = rdr.GetValue(0).ToString();
                UserRole = rdr.GetValue(1).ToString();
                Session.Add("UserName", UserName);
                Session.Add("UserRole", UserRole);
                FormsAuthentication.RedirectFromLoginPage(Login1.UserName, true);


            }
            else
            {
                Console.WriteLine("not available yet");
            }



            conn.Close();
                     

        }
    }
}
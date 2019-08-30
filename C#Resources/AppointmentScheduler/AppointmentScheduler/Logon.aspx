<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Logon.aspx.cs" Inherits="AppointmentScheduler.Logon" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        .auto-style1 {
            text-align: center;
        }
    </style>
    Log in Default Page
</head>
<body>
    <form id="form1" runat="server">
        <div class="auto-style1">
        <asp:Login ID="Login1" runat="server" Height="302px" OnAuthenticate="Login1_Authenticate" Width="1346px">
        </asp:Login>
        </div>
        <div>
            <br />
            <br />
        </div>
    </form>
</body>
&nbsp;
</html>

<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="LoginStatus.aspx.cs" Inherits="AppointmentScheduler.Work.LoginStatus" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    Header
</head>
<body>
    <form id="form1" runat="server">
        <div>
        </div>
        Login / Logout<br />
        <br />
        <asp:LoginStatus ID="LoginStatus1" runat="server" />
        <br />
        <br />
        <br />
        <br />
        <asp:HyperLink ID="HyperLink1" runat="server" NavigateUrl="~/Default.aspx">Home Page</asp:HyperLink>
        <br />
        <br />
    </form>
</body>
    Footer
</html>

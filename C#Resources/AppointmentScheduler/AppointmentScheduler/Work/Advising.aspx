<%@ Page Title="" Language="C#" MasterPageFile="~/MasterPage.Master" AutoEventWireup="true" CodeBehind="Advising.aspx.cs" Inherits="AppointmentScheduler.Work.messaging" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
    <style type="text/css">
        .auto-style7 {
            text-align: center;
            width: 732px;
            font-size: large;
        }
        .auto-style9 {
            text-align: center;
            font-size: large;
        }
        .auto-style10 {
            font-size: large;
        }
    </style>
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
    <p>
        <table style="width:100%;">
            <tr>
                <td class="auto-style7"><strong>Future Appointmnets</strong></td>
                <td class="auto-style9">
                    <asp:Label ID="Label1" runat="server" Text="Advisor Information:&nbsp;"></asp:Label>
                    <strong>&nbsp;
                    <asp:DropDownList ID="DropDownList1" runat="server" Height="25px" Width="227px" OnSelectedIndexChanged="DropDownList1_SelectedIndexChanged">
                    </asp:DropDownList>
                    </strong></td>
            </tr>
            <tr>
                <td class="auto-style9" colspan="2">
                    <asp:GridView ID="GridView1" runat="server" AutoGenerateColumns="False" DataSourceID="SqlDataSource2" Height="72px" Width="729px" OnSelectedIndexChanged="GridView1_SelectedIndexChanged">
                        <Columns>
                            <asp:CommandField ShowSelectButton="True" />
                            <asp:BoundField DataField="AppointmentDate" HeaderText="AppointmentDate" SortExpression="AppointmentDate" />
                            <asp:BoundField DataField="AppointmentReason" HeaderText="AppointmentReason" SortExpression="AppointmentReason" />
                            <asp:BoundField DataField="AppointmentID" HeaderText="AppointmentID" InsertVisible="False" ReadOnly="True" SortExpression="AppointmentID">
                            <ControlStyle BorderColor="White" />
                            <HeaderStyle ForeColor="White" />
                            <ItemStyle ForeColor="White" />
                            </asp:BoundField>
                        </Columns>
                    </asp:GridView>
                    <asp:SqlDataSource ID="SqlDataSource2" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString2 %>" SelectCommand="SELECT [AppointmentDate], [AppointmentReason], [AppointmentID] FROM [AppointmentTable] WHERE ([AdvisorID] = @AdvisorID)">
                        <SelectParameters>
                            <asp:SessionParameter DefaultValue="0" Name="AdvisorID" SessionField="AdvisorID" Type="Int32" />
                        </SelectParameters>
                    </asp:SqlDataSource>
                </td>
            </tr>
        </table>
    </p>
    <p>
        &nbsp;&nbsp;<asp:Button ID="Button1" runat="server" OnClick="Button1_Click" Text="Delete" Width="174px" />
&nbsp;&nbsp;
        <asp:Button ID="Button2" runat="server" Text="Schedule an Appointment" Width="231px" OnClick="Button2_Click" />
</p>
    <p>
        &nbsp;&nbsp; &nbsp;<span class="auto-style10">Date:</span>&nbsp;
        <asp:TextBox ID="TextBox2" runat="server" Width="209px"></asp:TextBox>
&nbsp;&nbsp;&nbsp; <span class="auto-style10">Time:
        <asp:TextBox ID="TextBox4" runat="server" Width="131px"></asp:TextBox>
&nbsp;&nbsp; Reason:</span>&nbsp;
        <asp:TextBox ID="TextBox3" runat="server" Width="337px" OnTextChanged="TextBox3_TextChanged"></asp:TextBox>
    </p>
    <p>
        &nbsp;</p>
</asp:Content>

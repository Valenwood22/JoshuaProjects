<%@ Page Title="" Language="C#" MasterPageFile="~/MasterPage.Master" AutoEventWireup="true" CodeBehind="messaging.aspx.cs" Inherits="AppointmentScheduler.Work.advising" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
    <style type="text/css">
    .auto-style7 {
        width: 402px;
    }
    .auto-style9 {
        height: 51px;
    }
    .auto-style11 {
        height: 26px;
    }
    .auto-style12 {
        font-size: medium;
    }
        .auto-style13 {
            text-align: justify;
            height: 312px;
        }
        .auto-style14 {
            text-align: left;
        }
    </style>
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
    <p>
        <table style="width: 100%;">
            <tr>
                <td class="auto-style7" rowspan="3">
                    <div class="auto-style13">
                        <asp:GridView ID="GridView1" runat="server" AllowPaging="True" AutoGenerateColumns="False" DataSourceID="SqlDataSource1" OnSelectedIndexChanged="GridView1_SelectedIndexChanged" ShowHeader="False" Width="448px">
                            <Columns>
                                <asp:CommandField ShowSelectButton="True" />
                                <asp:BoundField DataField="MSGDate" HeaderText="MSGDate" SortExpression="MSGDate" />
                                <asp:BoundField DataField="FromEmail" HeaderText="FromEmail" SortExpression="FromEmail" />
                                <asp:BoundField DataField="MSGtext" HeaderText="MSGtext" SortExpression="MSGtext" />
                            </Columns>
                            <RowStyle Wrap="True" />
                        </asp:GridView>
                        <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString2 %>" SelectCommand="SELECT [MSGDate], [FromEmail], [MSGtext] FROM [MSGTable] WHERE ([TOEmail] = @TOEmail)">
                            <SelectParameters>
                                <asp:SessionParameter DefaultValue="null" Name="TOEmail" SessionField="UserName" Type="String" />
                            </SelectParameters>
                        </asp:SqlDataSource>
                    </div>
                </td>
                <td class="auto-style11">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <asp:Label ID="Label1" runat="server" CssClass="auto-style12" Font-Size="Medium" Text="To:"></asp:Label>
&nbsp;
                    <asp:TextBox ID="TextBox2" runat="server" Height="23px" Width="433px"></asp:TextBox>
                </td>
            </tr>
            <tr>
                <td class="auto-style14">
                    <asp:TextBox ID="TextBox1" runat="server" Height="153px" Width="1066px" OnTextChanged="TextBox1_TextChanged2"></asp:TextBox>
                </td>
            </tr>
            <tr>
                <td class="auto-style9">
                    <asp:Button ID="Button1" runat="server" Text="Send" Width="114px" OnClick="Button1_Click" />
                &nbsp;&nbsp;
                    </td>
            </tr>
        </table>
</p>
</asp:Content>

<%@ Import Namespace="System.Data" %>
<%@ Import Namespace="MySql.Data.MySqlClient" %>

<body>
    <form id="form1" runat="server">
        <div>

            <asp:TextBox ID="roll" runat="server" />
            <asp:TextBox ID="name" runat="server" />
            <asp:TextBox ID="mark" runat="server" />
            <asp:Label ID="status" runat="server">
                <asp:Button ID="b1" runat="server" OnClick="b1c" />
        </div>
    </form>

    <script runat="server">
        public void b1c(object sender, EventArgs e) {

            MySqlConnection con = new MySqlConnection("server=localhost;database=cs;userid=root;password=gasc");
            con.Open();
            MySqlCommand cmd = new MySqlCommand("INSERT INTO firstmca(rno,name,mark) VALUES('" + roll.Text + "','" +
                name.Text + "','" + mark.Text + "')", con);
            int i = cmd.ExecuteNonQuery();
            if (i == 1) {
                status.Text = "Record Insert";
            } else {
                status.Text = "Error!";
            }
            con.Close();
        }

    </script>
</body>

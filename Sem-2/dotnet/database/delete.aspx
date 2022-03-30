<%@ Import Namespace="System.Data" %>
<%@ Import Namespace="MySql.Data.MySqlClient" %>

<body>
    <form id="form1" runat="server">
        <div>

            <asp:TextBox ID="roll" runat="server" />

            <asp:Label ID="status" runat="server">
                <asp:Button ID="b1" runat="server" OnClick="b1c" />
        </div>
    </form>

    <script runat="server">
        public void b1c(object sender, EventArgs e) {

            MySqlConnection con = new MySqlConnection("server=localhost;database=cs;userid=root;password=gasc");
            con.Open();
            MySqlCommand cmd = new MySqlCommand("DELETE FROM  firstmca  WHERE rno='" + roll.Text + "'", con);
            int i = cmd.ExecuteNonQuery();
            if (i == 1) {
                status.Text = "Record DELETE";
            } else {
                status.Text = "Error!";
            }
            con.Close();
        }

    </script>
</body>

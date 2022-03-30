 protected void Page_Load(object sender, EventArgs e)
        {
            jobStatus.Text = Session["msg"].ToString();

            name.Text = Session["sname"].ToString();
            age.Text = Session["sage"].ToString();
            gender.Text = Session["sgender"].ToString();
            exp.Text = Session["sexp"].ToString();
            jobs.Text = Session["sjob"].ToString();
        }
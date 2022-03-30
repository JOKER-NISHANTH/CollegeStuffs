
protected void Page_Load(object sender, EventArgs e)
{
    // Input Data Stored in Session
    Session["sname"] = name.Text;
    Session["sage"] = age.Text;
    Session["sgender"] = gender.SelectedValue;
    Session["semail"] = email.Text;
    Session["sexp"] = exp.Text;
    Session["sjob"] = job.SelectedValue;

}

protected void submit(object sender, EventArgs e)
{

    int expYear = int.Parse(exp.Text);
    string jobSelected = job.SelectedValue.ToString();


    if (expYear <= 2 && jobSelected == "Software Tester")
    {
        Session["msg"] = "You eligible  only for Software Tester Position";
        Response.Redirect("eligible.aspx");
    }
    else if ((expYear > 2 && expYear <= 5) && jobSelected == "Full Stack Developer")
    {
        Session["msg"] = "Yup!, You eligible for Software Tester as well as Full Stack Developer Position";
        Response.Redirect("eligible.aspx");
    }
    else if (expYear > 5 && jobSelected == "Web Pentester")
    {
        Session["msg"] = "Yeah!, You eligible for Software Tester , Full Stack Developer and Web Pentester Position";
        Response.Redirect("eligible.aspx");
    }


    else
    {
        ViewState["msg"] = "Whoops!, Sorry your experience has not met our criteria \n Thank you! \n Better luck Next time :)";
    }

    jobStatus.Text = ViewState["msg"].ToString();

}

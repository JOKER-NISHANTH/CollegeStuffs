<body>
    <form id="f1" runat="server">

        <center>

            <div>
                <!-- Name -->
                <asp:Label ID="lname" Text="Enter the name : " runat="server" />
                <asp:TextBox ID="name" runat="server" />
                <asp:RequiredFieldValidator ID="rname" runat="server" SetFocusOnError="true"
                    ErrorMessage="Please enter the name : " ControlToValidate="name" />

            </div>

            <div>
                <!-- Age -->
                <asp:Label ID="lage" Text="Enter the age : " runat="server" />
                <asp:TextBox ID="age" runat="server" />
                <asp:RangeValidator ID="rage" runat="server" MinimumValue="21" MaximumValue="30" Type="Integer"
                    SetFocusOnError="true" ErrorMessage="Not Eligible due to age limits [21-30 ] :) "
                    ControlToValidate="age" />

            </div>

            <div>
                <!-- Gender -->
                <asp:Label id="lgender" runat="server">Select your Gender : </asp:Label>

                <asp:RadioButtonList ID="gender" runat="server">

                    <asp:ListItem Selected="False" Value="Male">Male</asp:ListItem>
                    <asp:ListItem Selected="False" Value="Female">Female</asp:ListItem>

                </asp:RadioButtonList>

                <asp:RequiredFieldValidator ID="rgender" runat="server" ControlToValidate="gender"
                    ErrorMessage="Please pick the gender" SetFocusOnError="true" />

            </div>

            <div>
                <!-- Email -->
                <asp:Label ID="lemail" runat="server" Text="Enter your email : " />
                <asp:TextBox ID="email" runat="server" />
                <asp:RegularExpressionValidator ID="remail" runat="server" ControlToValidate="email"
                    ValidationExpression="\w+@\w+.com" SetFocusOnError="true" ErrorMessage="Invaild Email :)" />
            </div>


            <div>
                <!-- Experience -->
                <asp:Label id="lexp" runat="server">Enter your Experience</asp:Label>
                <asp:TextBox id="exp" runat="server"></asp:TextBox>

                <asp:RangeValidator id="rexp" runat="server" ControlToValidate="exp"
                    ErrorMessage="Not Eligible,due to age limit [1-10] :)" MaximumValue="10" MinimumValue="1"
                    SetFocusOnError="True" Type=" Integer" />

            </div>

            <div>
                <!-- Job -->
                <asp:Label id="ljob" runat="server">Select your Job</asp:Label>

                <asp:DropDownList id="job" runat="server">

                    <asp:ListItem Value="">Please Select</asp:ListItem>
                    <asp:ListItem Value="Software Tester" Text="Software Tester" />
                    <asp:ListItem Value="Full Stack Developer" Text="Full Stack Developer" />
                    <asp:ListItem Value="Web Pentester" Text="Web Pentester" />

                </asp:DropDownList>

                <asp:RequiredFieldValidator id="rjob" runat="server" ControlToValidate="job"
                    ErrorMessage="Please pick your job" SetFocusOnError="true" />

            </div>

            <div>
                <asp:Button ID="b2" runat="server" Text="Submit" OnClick="submit" Font-Bold="true"
                    ForeColor="DodgerBlue" Height="45" Width="150" />
            </div>

        </center>

    </form>

    <br /><br /><br />
    <hr />

    <asp:Label ID="jobStatus" runat="server" />

</body>

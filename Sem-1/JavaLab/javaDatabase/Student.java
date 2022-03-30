package javaDatabase;

import java.io.*;
import java.util.*;
import java.sql.*;

public class Student {

	public static void main(String[] args) throws SQLException {

		String uri = "jdbc:mysql://localhost:3306/student";
		String usr = "root";
		String pwd = "root";
		
		int id , age;;
		String name , addr , email;
		
		Connection con =null;
		ResultSet rs;
		PreparedStatement ps;
		
		Scanner in = new Scanner(System.in);
		
		try {
			
			Class.forName("com.mysql.cj.jdbc.Driver");
			con = DriverManager.getConnection(uri,usr,pwd);
			
			System.out.println(" Details ");
			System.out.println("Enter the id : ");
			id = in.nextInt();
			
			System.out.println("Enter the name : ");
			in.nextLine();
			name = in.nextLine();
			
			System.out.println("Enter the age : ");
			age = in.nextInt();
			
			System.out.println("Enter the address : ");
			in.nextLine();
			addr = in.nextLine();
			
			System.out.println("Enter the email : ");
			email = in.nextLine();
			
		
			String query = "insert into studentdata values(?,?,?,?,?);";
			
			ps = con.prepareStatement(query);
			ps.setInt(1, id);
			ps.setString(2, name);
			ps.setInt(3, age);
			ps.setString(4, addr);
			ps.setString(5, email);
			
			ps.executeUpdate();
			
			rs = ps.executeQuery("select * from studentdata;");
			System.out.println("Id \t Name \t\t Age \t\t Address \t Email");
			
			while(rs.next()) {
				System.out.println(rs.getInt(1)+"\t"+rs.getString(2)+"\t"+rs.getInt(3)+"\t"+rs.getString(4)+"\t"+rs.getString(5));
				
			}
								
		}
		
		catch (Exception e) {
			System.out.println("SQL Error");
		}
		
		finally {
			con.close();
		}
		
	}

}

import java.io.*;
import java.util.*;
import java.sql.*;

class Bank {
	
	public static void main(String[] args){
		
		String uri = "jdbc:mysql://localhost:3306/bankdetails";
		String usr = "root";
		String pwd = "root";
		Connection con;
		Statement stmt;
		ResultSet rs;
		
		try{
						
			Class.forName("com.mysql.jdbc.Driver");  
			con = DriverManager.getConnection(uri,usr,pwd);
			stmt = con.createStatement();
			rs = stmt.executeQuery("SELECT * from bank");
			System.out.println("AccNo Name Amount");
			while(rs.next()){
				
				System.out.println(rs.getString(1)+ " " +rs.getString(2) + " " +rs.getString(3));
				con.close();
				
			}
		
		}
		catch(Exception e){
			
			System.out.println(" Sql Error ");
			
		}
		
		
	}
	
	
}

<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
	<%@ page import="java.io.*" %>
	<% String bname = request.getParameter("bname"); %>
	
	<% out.println(bname + " Book details"); %>
	
	<% if(bname.equals("c")) { %>
	
		<table border=3 %>
			<tr>
				<th>Title</th> <th>Author</th> <th>Edition</th> <th>Price</th>
			</tr>
			<tr>
				<td>C Dummies</td> <td>Nisha</td> <td>2nd Edition<td> <td>5687</td>
			</tr>
			<tr>
				<td>C Advance</td> <td>Vasee</td> <td>4nd Edition</td> <td>6587</td>
			</tr>
			
		</table>
	
	<% } %>
	
	<% if(bname.equals("c++")) { %>
		<table border="3">
			<tr>
			<th>Title</th> <th>Author</th> <th>Edition</th> <th>Price</th>
			</tr>
			<tr>
			<td>C++ Dummines</td> <td>Surya</td> <td>1nd Edition</td> <td>4531</td>
			</tr>
			<tr>
			<td>C++ Advance</td> <td>Vasee</td> <td>4nd Edition</td> <td>9567</td>
			</tr>
		</table>
	<%} %>
	
	<% if(bname.equals("java")) { %>
		<table border="3">
			<tr>
			<th>Title</th> <th>Author</th> <th>Edition</th> <th>Price</th>
			</tr>
			<tr>
			<td>Java Dummines</td> <td>vijay</td> <td>3rd Edition</td> <td>4531</td>
			</tr>
			<tr>
			<td>Java Advance</td> <td>nisha</td> <td>7th Edition</td> <td>5627</td>
			</tr>
		</table>
	<%} %>
	
	<% if(bname.equals("python")) { %>
		<table border="3">
			<tr>
			<th>Title</th> <th>Author</th> <th>Edition</th> <th>Price</th>
			</tr>
			<tr>
			<td>Python Dummines</td> <td>vijay</td> <td>3rd Edition</td> <td>4531</td>
			</tr>
			<tr>
			<td>Python Advance</td> <td>nisha</td> <td>7th Edition</td> <td>5627</td>
			</tr>
		</table>
	<%} %>
	
</body>
</html>
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
	<%@ page import="java.lang.*" %>
	<center>Result for 	<%= request.getParameter("a") %></center>	
	
	<%
	
	int i = Integer.parseInt(request.getParameter("t1"));
	int j = Integer.parseInt(request.getParameter("t2"));
	int k =0;
	String str = request.getParameter("a");
	
	if(str.equals("add")) k = i + j;
	if(str.equals("sub")) k = i - j;
	if(str.equals("mul")) k = i * j;
	if(str.equals("div")) k = i / j;
	
	
	%>
	
	<center>Result <%= k %></center>
	
	
</body>
</html>
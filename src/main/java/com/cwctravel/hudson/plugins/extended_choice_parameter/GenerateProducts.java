/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.cwctravel.hudson.plugins.extended_choice_parameter;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.sql.*;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.sql.DriverManager;
import java.util.Properties;

/**
 *
 * @author ehhexxn
 */
public class GenerateProducts {
    
    public static String generateProduct(String propertiesFilename) {
        Connection conn = null;
        Statement statement = null;
        ResultSet rs = null;
        InputStream is = null;
        Properties prop = new Properties();
        try {
            Class.forName("com.mysql.jdbc.Driver").newInstance();
//                jdbc:mysql://host_name:port/dbname
            is = new FileInputStream(propertiesFilename);
            prop.load(is);
            
            System.out.println("Load Success");
            String url = "jdbc:mysql://" + prop.getProperty("host") + ":" + prop.getProperty("port") + "/" + prop.getProperty("db");
            String userName = prop.getProperty("user");
            String password = prop.getProperty("passwd");
            conn = DriverManager.getConnection(url, userName, password);
            System.out.println("Database connection established");
            statement = conn.createStatement();
            String QueryString = prop.getProperty("query");
            rs = statement.executeQuery(QueryString);
            StringBuilder sb = new StringBuilder();
            while (rs.next()) {
                sb.append(rs.getString(1) + ",");
                System.out.println(rs.getString(1));
            }
            return sb.toString();
        } catch (IOException ex) {
            Logger.getLogger(GenerateProducts.class.getName()).log(Level.SEVERE, null, ex);
        } catch (SQLException ex) {
            Logger.getLogger(GenerateProducts.class.getName()).log(Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            System.out.println(ex);
            Logger.getLogger(GenerateProducts.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            System.out.println(ex);
            Logger.getLogger(GenerateProducts.class.getName()).log(Level.SEVERE, null, ex);
        } catch (ClassNotFoundException ex) {
            System.out.println(ex);
            Logger.getLogger(GenerateProducts.class.getName()).log(Level.SEVERE, null, ex);
        }
        return "";
    }
}

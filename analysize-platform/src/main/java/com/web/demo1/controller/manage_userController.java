package com.web.demo1.controller;


import com.alibaba.fastjson.JSONObject;
import com.web.demo1.bean.manage.Manage_user;
import com.web.demo1.service.manageService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpServletRequest;
import java.util.List;

@Controller
@RequestMapping("/manage_userController")
public class manage_userController {
    @Autowired
    private manageService manage;
    @Autowired
    private HttpServletRequest request;

    @RequestMapping("getuser")
    @ResponseBody
    public Object queryUserList(int page, int limit){
        List<Manage_user> users = manage.getUser();
        List<Manage_user> user = manage.getUserbypage(page,limit);
        int a = users.size();
        JSONObject obj=new JSONObject();
        //前台通过key值获得对应的value值
        obj.put("code",0);
        obj.put("msg", "");
        obj.put("count",a);
        obj.put("data",user);
        return obj.toJSONString();
    }

    @RequestMapping("deleteuser")
    @ResponseBody
    public Object deleteUser(){
        String name = request.getParameter("name");
        int a = manage.deleteUser(name);
        JSONObject obj=new JSONObject();
        if (a == 1){
            obj.put("returnCode",200);
        }else{
            obj.put("returnCode",0);
        }
        return obj.toJSONString();
    }

    @RequestMapping("updateuser")
    @ResponseBody
    public Object updateUser(){
        String name = request.getParameter("name");
        String ID = request.getParameter("roleId");
        int a = manage.updateUser(ID,name);
        String role = manage.getroleNamebyId(ID);
        JSONObject obj=new JSONObject();
        if (a == 1){
            obj.put("returnCode",200);
            obj.put("returnRole",role);
        }else{
            obj.put("returnCode",0);
        }
        return obj.toJSONString();
    }

    @RequestMapping("getadmin")
    @ResponseBody
    public Object queryAdminList(int page, int limit){
        List<Manage_user> admins = manage.getAdmin();
        List<Manage_user> admin = manage.getAdminbypage(page,limit);
        int a = admins.size();
        JSONObject obj=new JSONObject();
        //前台通过key值获得对应的value值
        obj.put("code",0);
        obj.put("msg", "");
        obj.put("count",a);
        obj.put("data",admin);
        return obj.toJSONString();
    }

    @RequestMapping("deleteadmin")
    @ResponseBody
    public Object deleteAdmin(){
        String name = request.getParameter("name");
        int a = manage.deleteAdmin(name);
        JSONObject obj=new JSONObject();
        if (a == 1){
            obj.put("returnCode",200);
        }else{
            obj.put("returnCode",0);
        }
        return obj.toJSONString();
    }

    @RequestMapping("updateadmin")
    @ResponseBody
    public Object updateAdmin(){
        String name = request.getParameter("name");
        String password = request.getParameter("password");
        int a = manage.updateAdmin(password,name);
        JSONObject obj=new JSONObject();
        if (a == 1){
            String b = manage.getAdminpassword(name);
            obj.put("returnCode",200);
            obj.put("returnpass",b);
        }else{
            obj.put("returnCode",0);
        }
        return obj.toJSONString();
    }

    @RequestMapping("insertadmin")
    @ResponseBody
    public Object insertMenu(){
        String name = request.getParameter("name");
        String password = request.getParameter("password");
        int a = manage.addAdmin(name,password);
        JSONObject obj=new JSONObject();
        if (a == 1){
            obj.put("returnCode",200);
        }else{
            obj.put("returnCode",0);
        }
        return obj.toJSONString();
    }
}

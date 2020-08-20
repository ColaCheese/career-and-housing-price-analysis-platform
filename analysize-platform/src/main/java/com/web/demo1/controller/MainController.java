package com.web.demo1.controller;

import com.web.demo1.bean.user.User;
import com.web.demo1.service.manageService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class MainController {
    @Autowired
    private manageService manage;

    @RequestMapping("/")
    public String root() {
        return "redirect:/index";
    }

    @RequestMapping("/index")
    public String index() {
        return "index";
    }

    @RequestMapping("/reg")
    public String reg() {
        return "reg";
    }

    @RequestMapping("/forget")
    public String forget() {
        return "forget";
    }

    @RequestMapping("/login")
    public String login() {
        return "login";
    }

    @RequestMapping("/login-error")
    public String loginError(Model model) {
        model.addAttribute( "loginError"  , true);
        return "login";
    }

    @RequestMapping("/ifreg")
    @ResponseBody
    public String ifreg(String username) {
/*        System.out.println("对注册用户名判断");
        System.out.println(manage.getUserName(username));*/
       return manage.getUserName(username);
    }

    @RequestMapping("/toreg")
    @ResponseBody
    public String toreg(User user) {
        System.out.println(user.getUsername());
        manage.addUserAndUserRole(user);
        String reginfo = "regSuccessful";
        return reginfo;
    }

    @GetMapping("/401")
    public String accessDenied() {
        return "401";
    }

    @GetMapping("/user/common")
    public String common() {
        return "common";
    }

    @GetMapping("/user/admin")
    public String admin() {
        return "admin";
    }


}

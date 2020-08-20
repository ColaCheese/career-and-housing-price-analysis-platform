package com.web.demo1.controller;

import com.web.demo1.service.manageService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Controller
public class pageController {
    @Autowired
    manageService manage;
    @RequestMapping("/menumanage")
    public String menu(Model model){
        model.addAttribute( "Localmenus"  ,manage.getLocalmenu());
        return "admin-menumanage";
    }

    @RequestMapping("/rolemanage")
    public String role(){
        return "admin-rolemanage";
    }

    @RequestMapping("/usermanage")
    public String usermanage(Model model){
        model.addAttribute( "roles"  ,manage.getUserrole());
        return "admin-usermanage";
    }

    @RequestMapping("/adminmanage")
    public String adminmanage(){
        return "admin-adminmanage";
    }

    @RequestMapping("/analysismanage")
    public String analysismanage(){
        return "admin-analysismanage";
    }

    @RequestMapping("/role")
    public String rolemanage(){
        return "admin-rolemanage";
    }

    @RequestMapping("/analysis")
    public String selectInfo(Model model) {
        model.addAttribute( "citys"  ,manage.getSAllcity());
        model.addAttribute("trends",manage.getSAllTrend());
        model.addAttribute("anas",manage.getSAllAna());
        return "user-analysis";
    }

    @RequestMapping("/hotcity")
    public String hotcity(){
        return "hotCity";
    }

    @RequestMapping("/city")
    public String city(){
        return "ChinaMap";
    }

    @RequestMapping("/district")
    public String district(){
        return "district";
    }

    @RequestMapping("/cityName")
    public String cityName(){
        return "cityName";
    }
}

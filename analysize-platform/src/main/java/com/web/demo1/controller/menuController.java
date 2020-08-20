package com.web.demo1.controller;
import com.web.demo1.bean.manage.RoleMenu;
import com.web.demo1.bean.user.User;
import com.web.demo1.service.manageService;
import com.web.demo1.bean.manage.Menu;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpRequest;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContext;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import com.alibaba.fastjson.JSON;
import javax.servlet.http.HttpServletRequest;
import com.alibaba.fastjson.JSONObject;

import java.util.List;

@Controller
@RequestMapping("/menuController")
public class menuController {
    @Autowired
    private manageService manage;
    @Autowired
    private HttpServletRequest request;
    @RequestMapping("get")
    @ResponseBody
    public Object queryMenuList(int page, int limit){
        List<Menu> menus = manage.getMenuList();
        List<Menu> menu = manage.getMenuListbypage(page, limit);
        int a = menus.size();
        JSONObject obj=new JSONObject();
        //前台通过key值获得对应的value值
        obj.put("code",0);
        obj.put("msg", "");
        obj.put("count",a);
        obj.put("data",menu);
        return obj.toJSONString();
    }
    @RequestMapping("delete")
    @ResponseBody
    public Object deleteMenu(){
        String menuid = request.getParameter("menuId");
        manage.deleterolemenu(menuid);
        boolean a = manage.deleteMenu(menuid);
        JSONObject obj=new JSONObject();
        if (a){
            obj.put("returnCode",200);
        }else{
            obj.put("returnCode",0);
        }
        return obj.toJSONString();
    }
    @RequestMapping("update")
    @ResponseBody
    public Object updateMenu(){
        String menuId = request.getParameter("menuId");
        String menuName = request.getParameter("menuName");
        String parentID = request.getParameter("parentID");
        String URL = request.getParameter("menuURL");
        String description = request.getParameter("menudescription");
        boolean a = manage.updateMenu(menuName,URL,description,parentID,menuId);
        String b = manage.getMenuName(parentID);
        JSONObject obj=new JSONObject();
        if (a){
            obj.put("returnCode",200);
            obj.put("returnName",b);
        }else{
            obj.put("returnCode",0);
        }
        return obj.toJSONString();
    }
    @RequestMapping("insert")
    @ResponseBody
    public Object insertMenu(){
        String menuName = request.getParameter("menuName");
        String parentID = request.getParameter("parentID");
        String URL = request.getParameter("menuURL");
        String description = request.getParameter("menudescription");
        int a = manage.insertMenu(menuName,URL,description,parentID);
        String b = manage.getMenuName(parentID);
        JSONObject obj=new JSONObject();
        if (a != -1){
            obj.put("returnCode",a);
            obj.put("returnName",b);
        }else{
            obj.put("returnCode",-1);
        }
        return obj.toJSONString();
    }

    @RequestMapping("roleMenu")
    @ResponseBody
    public Object RoleMenu(Authentication authentication){
        SecurityContext ctx = SecurityContextHolder.getContext();
        Authentication auth = ctx.getAuthentication();
        User user = (User) auth.getPrincipal();
        String roleID =  user.getAuthorities().get(0).getRoleID();
        RoleMenu roleMenu = manage.queryRoleMenu(roleID);
        return roleMenu;
    }



    @RequestMapping("/anaInfo")
    @ResponseBody
    public Object anaInfo(String cityName,String trendName,String analysisID){
        System.out.println("分析的传值："+cityName+trendName+analysisID);
        return manage.getAnaAll(cityName,trendName,analysisID);
    }
}

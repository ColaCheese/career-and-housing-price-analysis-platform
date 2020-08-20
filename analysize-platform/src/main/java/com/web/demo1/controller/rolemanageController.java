package com.web.demo1.controller;


import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.web.demo1.bean.manage.Role;
import com.web.demo1.service.manageService;
import com.web.demo1.utils.dtree.DTree;
import com.web.demo1.utils.dtree.DTreeResponse;
import com.web.demo1.utils.dtree.Status;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpServletRequest;
import java.util.ArrayList;
import java.util.List;

@Controller
@RequestMapping("/roleController")
public class rolemanageController {
    @Autowired
    private manageService manage;
    @Autowired
    private HttpServletRequest request;

    @RequestMapping("getrole")
    @ResponseBody
    public Object queryRoleList(int page, int limit) {
        List<Role> roles = manage.getRole();
        List<Role> role = manage.getRolebypage(page, limit);
        int a = roles.size();
        JSONObject obj = new JSONObject();
        //前台通过key值获得对应的value值
        obj.put("code", 0);
        obj.put("msg", "");
        obj.put("count", a);
        obj.put("data", role);
        return obj.toJSONString();
    }

    @RequestMapping("deleterole")
    @ResponseBody
    public Object deleteRole() {
        String roleID = request.getParameter("roleID");
        int a = manage.deleteRole(roleID);
        JSONObject obj = new JSONObject();
        if (a != -1) {
            obj.put("returnCode", 200);
        } else {
            obj.put("returnCode", -1);
        }
        return obj.toJSONString();
    }

    @RequestMapping("insertrole")
    @ResponseBody
    public Object insertRole() {
        String roleName = request.getParameter("roleName");
        String roleIntro = request.getParameter("roleIntro");
        int a = manage.addRole(roleName, roleIntro);
        JSONObject obj = new JSONObject();
        if (a != -1) {
            obj.put("returnCode", a);
        } else {
            obj.put("returnCode", -1);
        }
        return obj.toJSONString();
    }

    @RequestMapping("getdtree")
    @ResponseBody
    public Object getdtree() {
        String roleID = request.getParameter("roleID");
        //System.out.print(roleID);
        List<DTree> dtrees = new ArrayList<DTree>();
        dtrees = manage.getTree(roleID);
        DTreeResponse resp = new DTreeResponse();
        Status status = new Status();
        resp.setData(dtrees);
        resp.setStatus(status);
        System.out.print(resp.getData());
        return resp;
    }

    @RequestMapping("update")
    @ResponseBody
    public Object updateauthority() {
        String data = request.getParameter("data");
        System.out.print(data);
        JSONArray jsonArray = JSON.parseArray(data);
        JSONObject jsonOne;
        int a = 0;
        for(int i=0;i<jsonArray.size();i++) {
            jsonOne = jsonArray.getJSONObject(i);
            String menuID = (String)jsonOne.get("nodeId");
            String roleID = (String)jsonOne.get("roleID");
            String checked = (String)jsonOne.get("checked");
            if(checked.equals("0")){//删除权限
               a = manage.deleteauthority(roleID,menuID);
            }else{//增加权限
               a = manage.addauthority(roleID,menuID);
            }
        }
        JSONObject obj=new JSONObject();
        if (a != 0){
            obj.put("returnCode",200);
        }else{
            obj.put("returnCode",0);
        }
        return obj.toJSONString();
    }
}

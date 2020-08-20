package com.web.demo1.controller;

import com.alibaba.fastjson.JSONObject;
import com.web.demo1.bean.city.Data;
import com.web.demo1.service.manageService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpServletRequest;
import java.util.List;

@Controller
@RequestMapping("/analysismanageController")
public class analysismanageController {

    @Autowired
    private manageService manage;
    @Autowired
    private HttpServletRequest request;

    @RequestMapping("getdata")
    @ResponseBody
    public Object queryDataList(int page, int limit){
        List<Data> datas = manage.getData();
        List<Data> data = manage.getDatabypage(page,limit);
        int a = datas.size();
        JSONObject obj=new JSONObject();
        //前台通过key值获得对应的value值
        obj.put("code",0);
        obj.put("msg", "");
        obj.put("count",a);
        obj.put("data",data);
        return obj.toJSONString();
    }

    @RequestMapping("deleteanalysis")
    @ResponseBody
    public Object deleteAnalysis(){
        String ID = request.getParameter("analysisID");
        int a = manage.deleteAnalysis(ID);
        JSONObject obj=new JSONObject();
        if (a == 1){
            obj.put("returnCode",200);
        }else{
            obj.put("returnCode",0);
        }
        return obj.toJSONString();
    }

    @RequestMapping("updateanalysis")
    @ResponseBody
    public Object updateAnalysis(){
        String ID = request.getParameter("analysisID");
        String percent = request.getParameter("percent");
        String years = request.getParameter("years");
        String rate = request.getParameter("rate");
        int a = manage.updateAnalysis(percent,years,rate,ID);
        JSONObject obj=new JSONObject();
        if (a == 1){
            obj.put("returnCode",200);
        }else{
            obj.put("returnCode",0);
        }
        return obj.toJSONString();
    }

    @RequestMapping("addanalysis")
    @ResponseBody
    public Object insertMenu(){
        String percent = request.getParameter("percent");
        String years = request.getParameter("years");
        String rate = request.getParameter("rate");
        int a = manage.addAnalysis(percent,years,rate);
        JSONObject obj=new JSONObject();
        if (a != -1){
            obj.put("returnCode",a);
        }else{
            obj.put("returnCode",-1);
        }
        return obj.toJSONString();
    }
}

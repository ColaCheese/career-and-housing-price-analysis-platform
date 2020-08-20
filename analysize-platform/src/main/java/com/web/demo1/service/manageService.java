package com.web.demo1.service;
import com.web.demo1.bean.city.Analysis;
import com.web.demo1.bean.city.Data;
import com.web.demo1.bean.manage.Manage_user;
import com.web.demo1.bean.manage.Menu;
import com.web.demo1.bean.manage.Role;
import com.web.demo1.bean.manage.RoleMenu;
import com.web.demo1.bean.user.User;
import com.web.demo1.utils.dtree.DTree;

import java.util.List;

public interface manageService {
    ////////////////////////////////////////////////////菜单管理//////////////////////////////////////////////////////
    public List<Menu> getMenuList();//返回菜单
    public boolean deleteMenu(String id);
    public boolean updateMenu(String menuName,String menuURL,String description,String parentId,String id);
    public int insertMenu(String menuName,String menuURL,String description,String parentId);
    public List<Menu> getMenuListbypage(int page, int pagesize);//返回菜单分页
    public List<Menu> getLocalmenu();
    public String getMenuName(String ID);
    public int deleterolemenu(String ID);
    ///////////////////////////////////////////////////功能用户管理///////////////////////////////////////////////////
    public List<Manage_user> getUser();//返回功能用户
    public List<Manage_user> getUserbypage(int page, int pagesize);//返回功能用户分页
    public int deleteUser(String name);
    public int updateUser(String ID,String name);
    public List<Role> getUserrole();//生成用户角色下拉框
    ////////////////////////////////////////////////系统用户管理/////////////////////////////////////////////
    public List<Manage_user> getAdmin();//返回系统用户
    public List<Manage_user> getAdminbypage(int page, int pagesize);//返回系统用户分页
    public int deleteAdmin(String name);
    public int updateAdmin(String password,String name);
    public int addAdmin(String name, String password);
    public String getAdminpassword(String userName);
    /////////////////////////////////////////////////分析管理/////////////////////////////////////////////
    public List<Data> getData();
    public List<Data> getDatabypage(int page,  int pagesize);
    public int deleteAnalysis(String ID);
    public int updateAnalysis(String percent, String years, String rate, String ID);
    public int addAnalysis(String percent, String years, String rate);
    ////////////////////////////////////////////////角色管理////////////////////////////////////////////
    public String getroleNamebyId(String ID);
    public int addRole(String roleName, String roleIntro);
    public int deleteRole(String ID);
    public List<Role> getRole();
    public List<Role> getRolebypage(int page, int pagesize);
    public List<DTree> getTree(String roleID);
    public int addauthority(String roleID, String menuID);
    public int deleteauthority(String roleID, String menuID);

    public RoleMenu queryRoleMenu(String roleID);
    public String getUserName(String username);
    public void addUserAndUserRole(User user);
    public List<String> getSAllcity();
    public List<String> getSAllTrend();
    public List<Data> getSAllAna();
    public Analysis getAnaAll(String cityName, String trendName, String analysisID);
}

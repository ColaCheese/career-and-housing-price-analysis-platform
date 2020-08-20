package com.web.demo1.service.serviceImpl;
import com.web.demo1.bean.city.Analysis;
import com.web.demo1.bean.city.Data;
import com.web.demo1.bean.city.Trend;
import com.web.demo1.bean.manage.Manage_user;
import com.web.demo1.bean.manage.Menu;
import com.web.demo1.bean.manage.Role;
import com.web.demo1.bean.manage.RoleMenu;
import com.web.demo1.bean.user.User;
import com.web.demo1.dao.*;
import com.web.demo1.service.manageService;
import com.web.demo1.utils.dtree.CheckArr;
import com.web.demo1.utils.dtree.DTree;
import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.util.DigestUtils;

import java.util.ArrayList;
import java.util.List;

@Service
public class manageServiceImpl implements manageService {
    @Autowired
    private menuMapper menumapper;
    @Autowired
    private admin_userMapper admin_usermapper;
    @Autowired
    private analysismanageMapper analysismanagemapper;
    @Autowired
    private roleMapper rolemapper;
    @Autowired
    private SelectMapper selectMapper;
    @Autowired
    private UserMapper userpper;

    /////////////////////////////////////////////////菜单管理//////////////////////////////////////////////////////////
    public List<Menu> getMenuList(){

        return menumapper.selectmenu();
}

    public boolean deleteMenu(String id){
        int a = menumapper.deletemenu(id);
        if(a>0){
            return true;
        }else{
            return false;
        }
    }

    // public int updatemenu(String menuName,String menuURL,String description,String parentId,String id);
    public boolean updateMenu(String menuName,String menuURL,String description,String parentId,String id){
        int a = menumapper.updatemenu(menuName, menuURL, description, parentId, id);
        if(a>0){
            return true;
        }else{
            return false;
        }
    }

    public int insertMenu(String menuName,String menuURL,String description,String parentId){
        int a = menumapper.insertmenu(menuName, menuURL, description, parentId);
        if(a == 1){
            return menumapper.getnewId();
        }else{
            return -1;
        }
    }

    public List<Menu> getMenuListbypage(int page, int pagesize){
        int start = (page-1)*pagesize;
        List<Menu> menus = menumapper.selectmenubypage(start, pagesize);
        for(Menu m : menus){
            if(!m.getParentID().equals("0")){
                String parentName = menumapper.getParentname(m.getParentID());
                m.setParentName(parentName);
            }
        }
        return menus;
    }

    public List<Menu> getLocalmenu(){
        return menumapper.getLocalmenu();
   }

   public String getMenuName(String ID){
        return menumapper.getMenuname(ID);
   }

    public int deleterolemenu(String ID){
        return menumapper.deleterolemenu(ID);
    }
//////////////////////////////////////////功能用户管理//////////////////////////////////////////////////////////////////////
    public List<Manage_user> getUser(){//返回功能用户
        return admin_usermapper.getuser();
    }
    public List<Manage_user> getUserbypage(int page, int pagesize){//返回功能用户分页
        int start = (page-1)*pagesize;
        return admin_usermapper.getuserbypage(start,pagesize);
    }
    public int deleteUser(String name){
        return admin_usermapper.deleteuser(name);
    }
    public int updateUser(String ID,String name){
        return admin_usermapper.updateuser(ID,name);
    }
    public List<Role> getUserrole(){//生成用户角色下拉框
        return rolemapper.getUserrole();
    }

    ///////////////////////////////////////系统用户管理/////////////////////////////////////////////////////////////////////////
    public List<Manage_user> getAdmin(){//返回系统用户
        return admin_usermapper.getadmin();
    }
    public List<Manage_user> getAdminbypage(int page, int pagesize){//返回系统用户分页
        int start = (page-1)*pagesize;
        return admin_usermapper.getadminbypage(start,pagesize);
    }
    public int deleteAdmin(String name){
        return admin_usermapper.deleteadmin(name);
    }
    public int updateAdmin(String password,String name){
        String pass = DigestUtils.md5DigestAsHex(password.getBytes());
        return admin_usermapper.updateadmin(pass,name);
    }
    public int addAdmin(String name, String password){
        String pass = DigestUtils.md5DigestAsHex(password.getBytes());
        return admin_usermapper.insertadmin(name,pass);
    }
    public String getAdminpassword(String userName){
        return admin_usermapper.getAdminpassword(userName);
    }
    ///////////////////////////////////////////分析管理///////////////////////////////////////////////////////////////////////////
    public List<Data> getData(){
        return analysismanagemapper.getData();
    }

    public List<Data> getDatabypage(int page,  int pagesize){
        int start = (page-1) * pagesize;
        return analysismanagemapper.getDatabypage(start, pagesize);
    }
    public int deleteAnalysis(String ID){
        return analysismanagemapper.deleteAnalysis(ID);
    }
    public int updateAnalysis(String percent, String years, String rate, String ID){
        return analysismanagemapper.updateAnalysis(percent,years,rate,ID);
    }
    public int addAnalysis(String percent, String years, String rate){
        int a = analysismanagemapper.addAnalyssis(percent,years,rate);
        if(a == 1){
            return analysismanagemapper.getnewId();
        } else{
            return -1;
        }
    }
////////////////////////////////////////////////角色管理///////////////////////////////////////////////////////////////
    public String getroleNamebyId(String ID){
        return rolemapper.getroleNamebyId(ID);
    }
    public int addRole(String roleName, String roleIntro){
        int a = rolemapper.addRole(roleName,roleIntro);
        if(a == 1){
            return rolemapper.getnewId();
        }else{
            return -1;
        }
    }
    public int deleteRole(String ID){
        List<User> candelete = rolemapper.candelete(ID);
        if(candelete.isEmpty()){
            rolemapper.deleteRolemenubyRoleid(ID);
            return rolemapper.deleterole(ID);
        }else{
            return -1;
        }
    }
    public List<Role> getRole(){
        return rolemapper.getRole();
    }
    public List<Role> getRolebypage(int page, int pagesize){
        int start = (page-1) * pagesize;
        return rolemapper.getRolebypage(start,pagesize);
    }
    public List<DTree> getTree(String roleID){
        List<Menu> menus = rolemapper.getMenu();
        List<Menu> menuCanget = rolemapper.getMenubyID(roleID);
        List<DTree> dtree = new ArrayList<DTree>();
        DTree d = null;
        CheckArr check = null;
        List<CheckArr> checklist = null;
        List<CheckArr> checklist2 = null;
        List<DTree> child = null;
        for(Menu menu : menus) {
            if (menu.getParentID().equals("0")) {
                child = new ArrayList<DTree>();
                d = new DTree();
                check = new CheckArr();
                check.setType("0");
                check.setChecked("0");
                d.setId(menu.getMenuId());
                d.setTitle(menu.getMenuName());
                d.setLast(false);
                for (Menu m : menuCanget) {
                    if (m.getMenuId().equals(menu.getMenuId())) {
                        check.setChecked("1");
                        break;
                    }
                }
                checklist = new ArrayList<CheckArr>();
                checklist.add(check);
                d.setCheckArr(checklist);
                for (Menu menu2 : menus) {
                    if (menu2.getParentID().equals(menu.getMenuId())) {
                        DTree d2 = new DTree();
                        check = new CheckArr();
                        check.setType("0");
                        check.setChecked("0");
                        d2.setId(menu2.getMenuId());
                        d2.setParentId(menu2.getParentID());
                        d2.setTitle(menu2.getMenuName());
                        d2.setLast(true);
                        for (Menu m : menuCanget) {
                            if (m.getMenuId().equals(menu2.getMenuId())) {
                                check.setChecked("1");
                                break;
                            }
                        }
                        checklist2 = new ArrayList<CheckArr>();
                        checklist2.add(check);
                        d2.setCheckArr(checklist2);
                        child.add(d2);
                    }
                }
                d.setChildren(child);
                dtree.add(d);
            }
        }
        return dtree;
    }

    public int addauthority(String roleID, String menuID){

        return rolemapper.addauthority(Integer.parseInt(roleID),Integer.parseInt(menuID));
    }
    public int deleteauthority(String roleID, String menuID){
        return rolemapper.deleteauthority(roleID,menuID);
    }



    public RoleMenu queryRoleMenu(String roleID) {
        List<String> menuIDs = menumapper.getRoleMenuId(roleID);
        List<RoleMenu> roleMenus = new ArrayList<RoleMenu>();
        List<RoleMenu> roleMenus1 = new ArrayList<RoleMenu>();
        RoleMenu roleMenu = new RoleMenu();
        roleMenu.setList(roleMenus1);
        roleMenu.setMenuID("0");
        roleMenu.setParentID("no");
        roleMenus.add(roleMenu);
        //循环寻找菜单属性
        for(String menuID : menuIDs){
            RoleMenu rolemenu = menumapper.getRoleMenu(menuID);
            List<RoleMenu> roleMenuss = new ArrayList<RoleMenu>();
            rolemenu.setList(roleMenuss);
            System.out.println(rolemenu);
            roleMenus.add(rolemenu);
        }
        System.out.println(roleMenus);
        //生成菜单
        int n = roleMenus.size();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(roleMenus.get(j).getParentID().equals(roleMenus.get(i).getMenuID()))
                    roleMenus.get(i).getList().add(roleMenus.get(j));
            }
        }
        roleMenu = roleMenus.get(0);
        return roleMenu;
    }

    @Override
    public String getUserName(String username) {
        String theusername = userpper.getUsername(username);
        String status = "";
        if (theusername != null) {
            status = "tuue";
            return status;
        }
        else{
            status = "faase";
            return status;
        }

    }

    @Override
    public void addUserAndUserRole(User user) {
        //System.out.println("旧的密码我看看："+ user.getPassword());
        String newpassword = DigestUtils.md5DigestAsHex(user.getPassword().toString().getBytes());
        user.setPassword(newpassword);
        //System.out.println("新的加密的密码我看看："+newpassword);
        userpper.addUser(user);
        String userID = userpper.getUserID(user.getUsername());
    }

    @Override
    public Analysis getAnaAll(String cityName, String trendName, String analysisID) {
        Analysis analysis = new Analysis();
        analysis.setCityName(cityName);
        Trend trend = selectMapper.getAnaTrend(cityName,trendName);
        trend.setTrendName(trendName);
        Data data = selectMapper.getOneAna(analysisID);
        Analysis analysis1 = selectMapper.getAnaRent(cityName);
        Analysis analysis2 = selectMapper.getAnaSold(cityName);
        analysis.setCityRentprice(analysis1.getCityRentprice());
        analysis.setCitySoldnum(analysis2.getCitySoldnum());
        analysis.setCitySoldprice(analysis2.getCitySoldprice());
        analysis.setCityRentnum(analysis1.getCityRentnum());
        analysis.setData(data);
        analysis.setTrend(trend);
        double rate= Double.valueOf(data.getRate());
        double years = Double.valueOf(data.getYears());
        double all = Double.valueOf(analysis.getCitySoldprice())*90*(1-Double.valueOf(data.getPercent())/100);
        double mothPay = all*(rate/12)*Math.pow((1+rate/12),years*12)/(Math.pow((1+rate/12),years*12)-1);
        double soldPercent = mothPay/Double.valueOf(analysis.getTrend().getTrendPrice())*100;
        double rentPercent = Double.valueOf(analysis.getCityRentprice())/Double.valueOf(analysis.getTrend().getTrendPrice())*100;
        analysis.setMothPay(String.format("%.2f",mothPay));
        analysis.setSoldPercent(String.format("%.2f",soldPercent));
        analysis.setRentPercent(String.format("%.2f",rentPercent));
        return  analysis;
    }

    @Override
    public List<Data> getSAllAna() {
        return selectMapper.getAllAna();
    }

    @Override
    public List<String> getSAllcity() {
        return selectMapper.getAllcity();
    }

    @Override
    public List<String> getSAllTrend() {
        return selectMapper.getAllTrend();
    }
}

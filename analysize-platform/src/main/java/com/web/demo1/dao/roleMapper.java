package com.web.demo1.dao;

import com.web.demo1.bean.manage.Menu;
import com.web.demo1.bean.manage.Role;
import com.web.demo1.bean.user.User;
import org.apache.ibatis.annotations.*;

import java.util.List;

@Mapper
public interface roleMapper {

    //@Select("select * from ")x
    @Select("select roleName from role where roleID = #{roleId}")
    public String getroleNamebyId(String ID);
    @Select("select roleID, roleName FROM role WHERE roleID > 2")
    public List<Role> getUserrole();
    ////////////////////////////////////////////////////////////////////////////////////////////////////
    @Select("select * from role")
    public List<Role> getRole();
    @Select("select * from role limit #{start},#{pagesize}")
    public List<Role> getRolebypage(@Param("start") int start,@Param("pagesize") int pagesize);
    @Insert("insert into role (roleName, roleIntro) VALUES (#{roleName},#{roleIntro})")
    public int addRole(@Param("roleName") String roleName,@Param("roleIntro") String roleIntro);
    @Delete("delete from role where roleID = #{roleId}")
    public int deleterole(String ID);
    @Select("select * from user where roleID = #{roleId}")
    public List<User> candelete(String ID);
    @Select("select LAST_INSERT_ID();")
    public int getnewId();
    @Select("SELECT menuID,menuName,parentID from menu")
    public List<Menu> getMenu();
    @Select("SELECT menuID from rolemenu WHERE roleID = #{roleId}")
    public List<Menu> getMenubyID(String ID);
    @Insert("insert into rolemenu (roleID, menuID) VALUES (#{roleID},#{menuID})")
    public int addauthority(@Param("roleID") int roleID,@Param("menuID") int menuID);
    @Delete("delete from rolemenu where roleID = #{roleID} and menuID = #{menuID}")
    public int deleteauthority(@Param("roleID") String roleID,@Param("menuID") String menuID);
    @Select("select roleID,roleName from role where roleID = #{roleID}")
    public Role getRolec(String roleID);

    @Delete("delete from rolemenu where roleID = #{roleID}")
    public void deleteRolemenubyRoleid(String roleID);
    @Select("select roleName from role where roleID = #{roleID}")
    public String getRoleName(String roleID);
}

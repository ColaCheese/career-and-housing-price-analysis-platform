package com.web.demo1.dao;

import com.web.demo1.bean.manage.Menu;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import com.web.demo1.bean.manage.RoleMenu;

import java.util.List;

@Mapper
public interface menuMapper {

    @Select("select menuID,menuName,menuUrl,menuDescription,parentID from menu")
    public List<Menu> selectmenu();
    @Delete("delete from menu where menuID = #{id}")
    public int deletemenu(String id);
    @Update("update menu set menuName = #{menuName} , menuUrl = #{menuURL},menuDescription = #{description},parentID = #{parentId} where menuID = #{id}")
    public int updatemenu( @Param("menuName") String menuName,@Param("menuURL") String menuURL,@Param("description") String description,@Param("parentId") String parentId,@Param("id") String id);
    @Insert("INSERT INTO menu (menuName, menuUrl, menuDescription, parentID) VALUES (#{menuName},#{menuURL},#{description},#{parentId})")
    public int insertmenu(@Param("menuName") String menuName,@Param("menuURL") String menuURL,@Param("description") String description,@Param("parentId") String parentId);
    @Select("select LAST_INSERT_ID();")
    public int getnewId();
    @Select("select * from menu limit #{start},#{pagesize}")
    public List<Menu> selectmenubypage(@Param("start") int start,@Param("pagesize") int pagesize);
    @Select("select menuName FROM menu WHERE menuID = #{id}")
    public String getParentname(String id);
    @Select("select menuName,menuID from menu where parentID = 0")
    public List<Menu> getLocalmenu();//返回根节点菜单
    @Select("select menuName from menu where menuID = #{id}")
    public String getMenuname(String id);
    @Delete("delete from rolemenu where menuID = #{id}")
    public int deleterolemenu(String id);
    //查找某用户的角色菜单权限
    @Select("select menuID from roleMenu where roleID = #{roleID};")
    public List<String> getRoleMenuId(String roleID);

    @Select("select menuID,menuName,menuUrl,parentID from menu where menuID = #{menuID};")
    public RoleMenu getRoleMenu(String menuID);

    @Select("select menuUrl from menu where menuID = #{menuID};")
    public String getMenuUrl(String menuID);
}

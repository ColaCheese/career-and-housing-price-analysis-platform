package com.web.demo1.bean.manage;

import java.util.List;

public class RoleMenu {
    private String  menuID;
    private String menuName;
    private String menuUrl;
    private List<RoleMenu> list;
    private String parentID;

    public String getMenuID() {
        return menuID;
    }

    public void setMenuID(String menuId) {
        this.menuID = menuId;
    }

    public String getMenuName() {
        return menuName;
    }

    public void setMenuName(String menuName) {
        this.menuName = menuName;
    }

    public String getMenuUrl() {
        return menuUrl;
    }

    public void setMenuUrl(String menuUrl) {
        this.menuUrl = menuUrl;
    }

    public List<RoleMenu> getList() {
        return list;
    }

    public void setList(List<RoleMenu> list) {
        this.list = list;
    }

    public String getParentID() {
        return parentID;
    }

    public void setParentID(String parentID) {
        this.parentID = parentID;
    }
}

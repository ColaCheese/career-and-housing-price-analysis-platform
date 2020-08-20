package com.web.demo1.bean.manage;

public class Menu {
    private String menuId;
    private String menuName;
    private String menuURL;
    private String menudescription;
    private String parentID;
    private String parentName;


    public String getMenuId() {
        return menuId;
    }

    public void setMenuId(String menuId) {
        this.menuId = menuId;
    }

    public String getMenuName() {
        return menuName;
    }

    public void setMenuName(String menuName) {
        this.menuName = menuName;
    }

    public String getMenuURL() {
        return menuURL;
    }

    public void setMenuURL(String menuURL) {
        this.menuURL = menuURL;
    }

    public String getMenudescription() {
        return menudescription;
    }

    public void setMenudescription(String menudescription) {
        this.menudescription = menudescription;
    }

    public String getParentID() {
        return parentID;
    }

    public void setParentID(String parentID) {
        this.parentID = parentID;
    }

    public String getParentName() {
        return parentName;
    }

    public void setParentName(String parentName) {
        this.parentName = parentName;
    }
}

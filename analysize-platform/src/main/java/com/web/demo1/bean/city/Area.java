package com.web.demo1.bean.city;

public class Area {
    private String areaName;
    private double areaSoldprice;
    private int areaSoldnum;
    private double areaRentprice;
    private String cityName;

    public String getCityName() {
        return cityName;
    }

    public void setCityName(String cityName) {
        this.cityName = cityName;
    }

    public String getAreaName() {
        return areaName;
    }

    public void setAreaName(String areaName) {
        this.areaName = areaName;
    }

    public double getAreaSoldprice() {
        return areaSoldprice;
    }

    public void setAreaSoldprice(double areaSoldprice) {
        this.areaSoldprice = areaSoldprice;
    }

    public int getAreaSoldnum() {
        return areaSoldnum;
    }

    public void setAreaSoldnum(int areaSoldnum) {
        this.areaSoldnum = areaSoldnum;
    }

    public double getAreaRentprice() {
        return areaRentprice;
    }

    public void setAreaRentprice(double areaRentprice) {
        this.areaRentprice = areaRentprice;
    }

}

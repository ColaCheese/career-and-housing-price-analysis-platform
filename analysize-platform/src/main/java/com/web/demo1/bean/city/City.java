package com.web.demo1.bean.city;
import java.util.List;

public class City {
    private String cityName;
    private double citySoldprice;
    private int citySoldnum;
    private double cityRentprice;
    private int cityRentnum;
    private double Trendprice;
    private int Trendnum;
    private List<Area> areaList;
    private List<Trend> trendList;

    public String getCityName() {
        return cityName;
    }

    public void setCityName(String cityName) {
        this.cityName = cityName;
    }

    public double getCitySoldprice() {
        return citySoldprice;
    }

    public void setCitySoldprice(double citySoldprice) {
        this.citySoldprice = citySoldprice;
    }

    public int getCitySoldnum() {
        return citySoldnum;
    }

    public void setCitySoldnum(int citySoldnum) {
        this.citySoldnum = citySoldnum;
    }

    public double getCityRentprice() {
        return cityRentprice;
    }

    public void setCityRentprice(double cityRentprice) {
        this.cityRentprice = cityRentprice;
    }

    public int getCityRentnum() {
        return cityRentnum;
    }

    public void setCityRentnum(int cityRentnum) {
        this.cityRentnum = cityRentnum;
    }

    public double getAverageTrendprice() {
        return Trendprice;
    }

    public void setAverageTrendprice(double averageTrendprice) {
        this.Trendprice = averageTrendprice;
    }

    public int getAverageTrendnum() {
        return Trendnum;
    }

    public void setAverageTrendnum(int averageTrendnum) {
        this.Trendnum = averageTrendnum;
    }

    public List<Area> getAreaList() {
        return areaList;
    }

    public void setAreaList(List<Area> areaList) {
        this.areaList = areaList;
    }

    public List<Trend> getTrendList() {
        return trendList;
    }

    public void setTrendList(List<Trend> trendList) {
        this.trendList = trendList;
    }
}

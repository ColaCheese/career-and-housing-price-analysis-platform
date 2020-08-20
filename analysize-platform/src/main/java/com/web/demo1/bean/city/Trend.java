package com.web.demo1.bean.city;

public class Trend {
    private String trendName;
    private int trendNum;
    private double trendPrice;
    private String cityName;

    public String getTrendName() {
        return trendName;
    }

    public void setTrendName(String trendName) {
        this.trendName = trendName;
    }

    public String getcityName() {
        return cityName;
    }

    public void setcityName(String cityName) {
        this.cityName = cityName;
    }

    public int getTrendNum() {
        return trendNum;
    }

    public void setTrendNum(int trendNum) {
        this.trendNum = trendNum;
    }

    public double getTrendPrice() {
        return trendPrice;
    }

    public void setTrendPrice(double trendPrice) {
        this.trendPrice = trendPrice;
    }
}

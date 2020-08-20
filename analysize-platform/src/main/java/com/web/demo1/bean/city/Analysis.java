package com.web.demo1.bean.city;

public class Analysis {
    private String cityName;
    private Trend trend;
    private String citySoldprice;
    private String citySoldnum;
    private String cityRentprice;
    private String cityRentnum;
    private Data data;
    private String mothPay;
    private String soldPercent;
    private String rentPercent;

    public String getCityRentnum() {
        return cityRentnum;
    }

    public void setCityRentnum(String cityRentnum) {
        this.cityRentnum = cityRentnum;
    }

    public String getCityName() {
        return cityName;
    }

    public void setCityName(String cityName) {
        this.cityName = cityName;
    }

    public Trend getTrend() {
        return trend;
    }

    public void setTrend(Trend trend) {
        this.trend = trend;
    }

    public String getCitySoldprice() {
        return citySoldprice;
    }

    public void setCitySoldprice(String citySoldprice) {
        this.citySoldprice = citySoldprice;
    }

    public String getCitySoldnum() {
        return citySoldnum;
    }

    public void setCitySoldnum(String citySoldnum) {
        this.citySoldnum = citySoldnum;
    }

    public String getCityRentprice() {
        return cityRentprice;
    }

    public void setCityRentprice(String cityRentprice) {
        this.cityRentprice = cityRentprice;
    }

    public Data getData() {
        return data;
    }

    public void setData(Data data) {
        this.data = data;
    }

    public String getMothPay() {
        return mothPay;
    }

    public void setMothPay(String mothPay) {
        this.mothPay = mothPay;
    }

    public String getSoldPercent() {
        return soldPercent;
    }

    public void setSoldPercent(String soldPercent) {
        this.soldPercent = soldPercent;
    }

    public String getRentPercent() {
        return rentPercent;
    }

    public void setRentPercent(String rentPercent) {
        this.rentPercent = rentPercent;
    }
}

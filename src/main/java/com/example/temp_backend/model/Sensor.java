package com.example.temp_backend.model;

import jakarta.persistence.*;

@Entity
@Table(name = "sensor")
public class Sensor {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @ManyToOne
    @JoinColumn(name = "herstellerid")
    private Hersteller hersteller;
    @ManyToOne
    @JoinColumn(name = "servercabinid")
    private ServerCabin serverCabin;
    @Column(name = "sensoraddress")
    private String sensorAddress;
    @Column(name = "maxtemp")
    private double maxTemp;

    public Sensor(Hersteller hersteller, ServerCabin serverCabin, String sensorAddress, double maxTemp) {
        this.hersteller = hersteller;
        this.serverCabin = serverCabin;
        this.sensorAddress = sensorAddress;
        this.maxTemp = maxTemp;
    }

    public Sensor(ServerCabin serverCabin) {
        this.serverCabin = serverCabin;
    }

    public Sensor(String sensorAddress) {
        this.sensorAddress = sensorAddress;
    }

    public Sensor(double maxTemp) {
        this.maxTemp = maxTemp;
    }

    public Sensor() {
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Hersteller getHersteller() {
        return hersteller;
    }

    public void setHersteller(Hersteller hersteller) {
        this.hersteller = hersteller;
    }

    public ServerCabin getServerCabin() {
        return serverCabin;
    }

    public void setServerCabin(ServerCabin serverCabin) {
        this.serverCabin = serverCabin;
    }

    public String getSensorAddress() {
        return sensorAddress;
    }

    public void setSensorAddress(String sensorAddress) {
        this.sensorAddress = sensorAddress;
    }

    public double getMaxTemp() {
        return maxTemp;
    }

    public void setMaxTemp(double maxTemp) {
        this.maxTemp = maxTemp;
    }
}

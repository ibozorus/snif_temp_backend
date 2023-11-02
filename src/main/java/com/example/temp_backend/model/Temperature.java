package com.example.temp_backend.model;

import jakarta.persistence.*;

import java.util.Date;

@Entity
@Table(name = "temperature")
public class Temperature {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @ManyToOne
    @JoinColumn(name = "sensorfk")
    private Sensor sensor;
    private double value;
    private Date timestamp;

    public Temperature(Sensor sensor, double value, Date timestamp) {
        this.sensor = sensor;
        this.value = value;
        this.timestamp = timestamp;
    }

    public Temperature() {
    }

    public Sensor getSensor() {
        return sensor;
    }

    public void setSensor(Sensor sensor) {
        this.sensor = sensor;
    }

    public double getValue() {
        return value;
    }

    public void setValue(double value) {
        this.value = value;
    }

    public Date getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(Date timestamp) {
        this.timestamp = timestamp;
    }
}

package com.example.temp_backend.model;

import jakarta.persistence.*;

import java.util.Date;

@Entity
@Table(name = "changelog")
public class ChangeLog {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @ManyToOne
    @JoinColumn(name = "sensorid")
    private Sensor sensor;
    @ManyToOne
    @JoinColumn(name = "userid")
    private User user;
    private Date datum;

    public ChangeLog() {
    }

    public ChangeLog(Sensor sensor, User user, Date datum) {
        this.sensor = sensor;
        this.user = user;
        this.datum = datum;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Sensor getSensor() {
        return sensor;
    }

    public void setSensor(Sensor sensor) {
        this.sensor = sensor;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    public Date getDatum() {
        return datum;
    }

    public void setDatum(Date datum) {
        this.datum = datum;
    }
}

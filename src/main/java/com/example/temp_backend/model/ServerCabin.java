package com.example.temp_backend.model;

import jakarta.persistence.*;

@Entity
@Table(name = "servercabin")
public class ServerCabin {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private int floor;

    public ServerCabin(int floor) {
        this.floor = floor;
    }

    public ServerCabin() {
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public int getFloor() {
        return floor;
    }

    public void setFloor(int floor) {
        this.floor = floor;
    }
}

package com.example.temp_backend.model;

import jakarta.persistence.*;

@Entity
@Table(name = "hersteller")
public class Hersteller {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String brand;

    public Hersteller() {
    }

    public Hersteller(String name) {
        this.brand = name;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

}

# ALX Project Nexus

# 🚀 ALX Project Nexus — Backend Engineering Knowledge

Welcome to **ALX Project Nexus**, a central repository documenting all major learnings, patterns, system designs, tools, challenges, and best practices gained throughout the **ProDev Backend Engineering Program**.

This repository acts as a **knowledge base** and a **reference guide** for backend developers building scalable, secure, production-grade backend systems — similar to real-world applications such as:

- Airbnb Clone (Property, booking & payment systems)
- Movie Recommendation Backend (Caching, external API integration)
- E-commerce, CRM, and high-performance API-driven systems

# 1. Overview of the ProDev Backend Engineering Program

The ProDev Backend Engineering program focuses on building **high-performance, secure, scalable backend systems** using industry-standard tools such as:

- **Django + Django REST Framework**
- **GraphQL APIs**
- **Celery & RabbitMQ**
- **PostgreSQL**
- **Redis caching**
- **External API integration**
- **Docker containerization**
- **CI/CD pipelines**
- **System Design & Scalability**

It mirrors real-world enterprise backend development and prepares engineers for professional engineering teams.

---

# 2. Core Technologies Covered

### **Programming**
- Python 3.x  

### **Backend Frameworks**
- Django  
- Django REST Framework  
- Graphene-Django (GraphQL)

### **Databases**
- PostgreSQL  
- SQLite (dev)  

### **Message Queues & Background Processing**
- Celery  
- RabbitMQ  

### **Caching & Optimization**
- Redis (caching, rate limiting, session store)

### **DevOps & Deployment**
- Docker & Docker Compose  
- Render deployment  
- GitHub Actions (CI/CD)

### **API Documentation**
- Swagger / drf-yasg  
- OpenAPI 3.0  

---
# 3. Major Backend Development Concepts Learned

### ✔ RESTful API Design  
### ✔ GraphQL Query Language  
### ✔ Database Schema Design  
### ✔ ORM Query Optimization  
### ✔ Authentication & Authorization (JWT / Token Auth)  
### ✔ Caching Strategies (Redis, per-view caching, low-level caching)  
### ✔ Asynchronous Tasks (Celery + RabbitMQ)  
### ✔ External API Integration  
### ✔ Logging & Monitoring  
### ✔ CI/CD Automation  
### ✔ Docker Image Creation & Deployment  

---

# 4. Case Study: Airbnb Clone Backend

A complete backend system built to simulate Airbnb.

### 🔑 Features Implemented
#### **User Management**
- Registration  
- JWT authentication  
- Profile updates  

#### **Property Management**
- CRUD endpoints  
- Filtering, search, indexing  

#### **Booking System**
- Availability checks  
- Booking lifecycle management  

#### **Payment Processing**
- Payment tracking endpoint  
- Optional integration with Stripe  

#### **Review System**
- Ratings and text reviews  

#### **Performance**
- Redis caching  
- Query optimization  
- DB indexing  

#### **API Documentation**
- Swagger UI  
- OpenAPI 3.0  

#### **GraphQL API**
Provides flexible nested data querying

#  MY PROJECT NEXUS 

# 🎬 Movie Recommendation API

A lightweight and efficient Movie Recommendation API built with
**Python**, **FastAPI**, and **machine learning techniques**.\
This API allows users to query movie recommendations, search movies, and
access metadata using a clean RESTful interface.

------------------------------------------------------------------------

## 🚀 Project Overview

The Movie Recommendation API provides:

- Trending & recommended movies

- JWT-based authentication

- Favorite movie management

- High-performance caching using Redis

- Background tasks using Celery

- TMDb integration for real movie data

- Full API docs with Swagger

This backend mirrors real-world production systems focusing on performance, scalability, clean code, and developer experience.

## 🚀 Features

-   Content-based movie recommendations\
-   Movie search by title\
-   Fetch movie metadata (genres, overview, poster, rating)\
-   FastAPI auto-generated interactive docs (Swagger & ReDoc)\
-   Clean modular structure for easy extension\
-   Ready for deployment on Render, Railway, or Docker
  
## 🛠 Tech Stack

Component	Technology
Backend Framework	Django, Django REST Framework
Authentication	JWT (SimpleJWT)
External API	TMDb API
Caching	Redis
Async Tasks	Celery + RabbitMQ
Database	PostgreSQL
Documentation	Swagger / drf-yasg
Deployment	Docker + Render


## 📦 Features

#### 🎞 Movie Endpoints

- Fetch trending movies
- Fetch recommended movies
- Movie search by title
- Error handling for external API failures

#### 🔐 Authentication
- Register users
- Login using JWT
- Secure endpoints for favorites

#### ⭐ Favorites Management
- Add a movie to favorites
- Remove from favorites
- Get user’s favorite movies

#### ⚡ Performance Optimization
- Redis caching for trending & recommended movies
- Cached responses reduce TMDb API usage
- Celery tasks update cached data automatically

#### 📘 API Documentation
- Swagger UI available


## 🧪 API Endpoints

#### Movies

Method	     Endpoint	                        Description
- GET	       /api/movies/trending/	          Get trending movies
  
- GET	       /api/movies/recommended/	        Get recommended movies
  
- GET	       /api/movies/search/?query=name	  Search movies

#### Authentication

Method	      Endpoint	                   Description
- POST	      /api/auth/register/	         Register user
- POST	      /api/auth/login/	           Login & get JWT

#### Favorites

Method	      Endpoint	                   Description
- POST	      /api/users/favorites/       	Add movie to favorites
- GET	        /api/users/favorites/	        Get favorite movies
- DELETE	    /api/users/favorites/{id}/	  Remove favorite

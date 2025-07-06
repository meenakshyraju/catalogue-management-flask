-- Create the database
CREATE DATABASE IF NOT EXISTS CatalogueDB;
USE CatalogueDB;

-- 1. Catalogue Table
CREATE TABLE IF NOT EXISTS Catalogue (
    catalogue_id INT AUTO_INCREMENT PRIMARY KEY,
    catalogue_name VARCHAR(100) NOT NULL,
    catalogue_description TEXT,
    start_date DATE,
    end_date DATE
);

-- 2. Product Table
CREATE TABLE IF NOT EXISTS Product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    product_description TEXT
);

-- 3. Category Table
CREATE TABLE IF NOT EXISTS Category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    category_description TEXT
);

-- 4. SKU Table
CREATE TABLE IF NOT EXISTS SKU (
    sku_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    sku_code VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2),
    stock_quantity INT,
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

-- 5. SKU_Attribute Table
CREATE TABLE IF NOT EXISTS SKU_Attribute (
    attribute_id INT AUTO_INCREMENT PRIMARY KEY,
    sku_id INT,
    attribute_name VARCHAR(100),
    attribute_value VARCHAR(100),
    FOREIGN KEY (sku_id) REFERENCES SKU(sku_id)
);

-- 6. Catalogue_Category_Map Table
CREATE TABLE IF NOT EXISTS Catalogue_Category_Map (
    id INT AUTO_INCREMENT PRIMARY KEY,
    catalogue_id INT,
    category_id INT,
    FOREIGN KEY (catalogue_id) REFERENCES Catalogue(catalogue_id),
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

-- 7. Category_Subcategory_Map Table
CREATE TABLE IF NOT EXISTS Category_Subcategory_Map (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parent_category_id INT,
    subcategory_id INT,
    FOREIGN KEY (parent_category_id) REFERENCES Category(category_id),
    FOREIGN KEY (subcategory_id) REFERENCES Category(category_id)
);

-- 8. Category_Product_Map Table
CREATE TABLE IF NOT EXISTS Category_Product_Map (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT,
    product_id INT,
    FOREIGN KEY (category_id) REFERENCES Category(category_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

-- 9. Users Table
CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);


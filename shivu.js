const mysql = require("mysql2/promise");

async function database() {
    try {
        const db = await mysql.createConnection({
            host: "localhost",
            user: "root",
            password: "S@Shivu_17",
            database: "voiceassistant"
        });

        console.log("✅ Connected to MySQL successfully!");
        return db;

    } catch (error) {
        console.error("❌ Connection failed:", error.message);
    }
}

database();
use actix_web::{web, App, HttpServer, HttpResponse, Responder};
use serde_json::json;
use std::time::Duration;
use tokio::time::sleep;
use log::{info, error};

async fn ping() -> impl Responder {
    info!("Handling /ping request");
    HttpResponse::Ok().json(serde_json::json!({"message": "pong"}))
}

async fn sleep_sync() -> impl Responder {
    // Simulate a synchronous sleep
    std::thread::sleep(Duration::from_secs(1));
    info!("Handling /sleep-sync request");
    HttpResponse::Ok().json(serde_json::json!({"message": "Synchronous sleep complete"}))
}

async fn sleep_async() -> impl Responder {
    // Simulate an asynchronous sleep
    sleep(Duration::from_secs(1)).await;
    info!("Handling /sleep-async request");
    HttpResponse::Ok().json(serde_json::json!({"message": "Asynchronous sleep complete"}))
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    // Initialize logging
    env_logger::init();

    info!("Starting server at http://127.0.0.1:8052");

    HttpServer::new(|| {
        App::new()
            .route("/api/ping/", web::get().to(ping))
            .route("/api/sleep-sync/", web::get().to(sleep_sync))
            .route("/api/sleep-async/", web::get().to(sleep_async))
    })
    .bind("0.0.0.0:8052")?
    .run()
    .await
}

use web_view::*;
use std::fs;

fn main() {

    let html_content = fs::read_to_string("src/index.html").expect("man wher tf the html file");
	
    web_view::builder()
        .title("My Project")
        .content(Content::Html(html_content))
        .size(320, 480)
        .resizable(true)
        .debug(true)
        .user_data(())
        .invoke_handler(|_webview, _arg| Ok(()))
        .run()
        .unwrap();
    
}
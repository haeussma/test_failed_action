```mermaid
classDiagram
    User *-- Image
    
    class User {
        +string name
        +string email
        +Image image
    }
    
    class Image {
        +string url
        +float size
    }
    
```
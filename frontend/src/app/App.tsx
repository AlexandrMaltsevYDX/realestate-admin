import "./App.scss";
import { Card } from "react-bootstrap";

function App() {
    const cardData = [
        {
            name: "жопа коня",
            category: "Category 1",
            description: "Descriptions 1",
            img: "This is img",
        },
        {
            name: "Card 2",
            category: "Category 2",
            description: "Descriptions 2",
            img: "This is img",
        },
        {
            name: "Card 3",
            category: "Category 3",
            description: "Descriptions 3",
            img: "This is img",
        },
    ];

    return (
        <>
            {cardData.map((card, index) => (
                <Card key={index}>
                    <Card.Body>
                        <Card.Title>{card.name}</Card.Title>
                        <Card.Text>{card.description}</Card.Text>
                    </Card.Body>
                </Card>
            ))}
        </>
    );
}

export default App;

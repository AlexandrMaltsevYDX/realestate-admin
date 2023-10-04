import "./App.scss";
import MainLayout from "../components/layouts/MainLayout/MainLayout";
import { BrowserRouter } from "react-router-dom";

function App() {
    return (
        <>
            <BrowserRouter>
                <MainLayout />
            </BrowserRouter>
        </>
    );
}

export default App;

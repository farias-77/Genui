import { Container } from "./styles";

import Sidebar from "../../components/Sidebar";
import Content from "../../components/Content";
import Content2 from "../../components/Content2";

export default function Home() {
    function generateRandomBinary() {
        return Math.floor(Math.random() * 2);
    }

    return (
        <Container>
            <Sidebar />
            {generateRandomBinary() ? <Content /> : <Content2 />}
        </Container>
    );
}

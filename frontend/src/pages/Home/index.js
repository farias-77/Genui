import { Container } from "./styles";

import Sidebar from "../../components/Sidebar";
import Content from "../../components/Content";

export default function Home() {
    return (
        <Container>
            <Sidebar />
            <Content />
        </Container>
    );
}

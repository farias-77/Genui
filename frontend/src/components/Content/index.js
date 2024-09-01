import { FaArrowRight } from "react-icons/fa6";
import { RiAccountCircleLine } from "react-icons/ri";

import {
    Container,
    GeneratedContent,
    AccountSummary,
    Header,
    Suggestions,
    Suggestion,
    Profile,
    Balance,
    GrayBox,
    DaySummary,
    Predictions,
} from "./styles";

export default function Content() {
    function getFormattedCurrentDate() {
        const meses = [
            "jan",
            "fev",
            "mar",
            "abr",
            "mai",
            "jun",
            "jul",
            "ago",
            "set",
            "out",
            "nov",
            "dez",
        ];
        const dataAtual = new Date();
        const dia = dataAtual.getDate();
        const mes = meses[dataAtual.getMonth()];

        return `${dia} ${mes}`;
    }

    function getTomorrowDayMonth() {
        const meses = [
            "janeiro",
            "fevereiro",
            "março",
            "abril",
            "maio",
            "junho",
            "julho",
            "agosto",
            "setembro",
            "outubro",
            "novembro",
            "dezembro",
        ];

        const dataAtual = new Date();
        const dataAmanha = new Date(dataAtual);
        dataAmanha.setDate(dataAtual.getDate() + 1);

        const dia = dataAmanha.getDate();
        const mes = meses[dataAmanha.getMonth()];

        return `${dia} de ${mes}`;
    }

    return (
        <Container>
            <GeneratedContent>
                <Header>
                    <h1>Insights e sugestões de tarefas</h1>
                    <div>
                        {(() => {
                            const date = getFormattedCurrentDate();
                            const dateArray = date.split(" ");
                            return (
                                <>
                                    <p>{dateArray[0]}</p>
                                    <span>{dateArray[1]}</span>
                                </>
                            );
                        })()}
                    </div>
                </Header>
                <Suggestions>
                    <div>
                        <p>Ver todos</p>
                        <div>
                            <FaArrowRight />
                        </div>
                    </div>
                    <Suggestion>
                        <h1>Previsão de inadimplência</h1>
                        <p>
                            sit amet consectetur. Sit pretium bibendum sem
                            vestibulum morbi quis odio. Magnis turpis in vitae
                            risus habitant tempor metus placerat.
                        </p>
                        <div>
                            <p>Ver detalhes</p>
                            <div>
                                <FaArrowRight />
                            </div>
                        </div>
                    </Suggestion>
                </Suggestions>
            </GeneratedContent>
            <AccountSummary>
                <Profile>
                    <h1>Peter Otto</h1>
                    <RiAccountCircleLine />
                </Profile>
                <Balance>
                    <h1>Sua conta</h1>
                    <p>R$ 2.000,00</p>
                    <div>
                        <GrayBox
                            width="49%"
                            height="40px"
                            color="#5DF186"
                            rotate="rotate(-90deg)"
                        >
                            <p>
                                <FaArrowRight />
                                Entradas
                            </p>
                            <p>R$ 1.000,00</p>
                        </GrayBox>
                        <GrayBox
                            width="49%"
                            height="40px"
                            color="#F15D5D"
                            rotate="rotate(90deg)"
                        >
                            <p>
                                <FaArrowRight />
                                Saídas
                            </p>
                            <p>R$ 1.000,00</p>
                        </GrayBox>
                    </div>
                </Balance>
                <DaySummary>
                    <h1>Fechamento</h1>
                    <div>
                        <GrayBox
                            width="49%"
                            height="80px"
                            flexDirection="column"
                            alignItems="flex-start"
                        >
                            <h3>Último fechamento</h3>
                            <h3>R$ 1.000,00</h3>
                        </GrayBox>
                        <GrayBox
                            width="49%"
                            height="80px"
                            flexDirection="column"
                            alignItems="flex-start"
                        >
                            <h3>Previsão de fechamento para hoje</h3>
                            <h3>R$ 1.000,00</h3>
                        </GrayBox>
                    </div>
                </DaySummary>
                <Predictions>
                    <h1>
                        Previsões para amanhã{" "}
                        <span>{getTomorrowDayMonth()}</span>
                    </h1>
                    <div>
                        <div>
                            <h2>Fechamento</h2>
                            <GrayBox>R$109.078</GrayBox>
                        </div>
                        <div>
                            <h2>Entradas</h2>
                            <GrayBox>R$109.078</GrayBox>
                        </div>
                        <div>
                            <h2>Saídas</h2>
                            <GrayBox>R$109.078</GrayBox>
                        </div>
                    </div>
                </Predictions>
            </AccountSummary>
        </Container>
    );
}

import { useState, useEffect } from "react";
import { RiAccountCircleLine } from "react-icons/ri";
import { FaArrowRight } from "react-icons/fa6";
import axios from "axios";

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
    ChartData,
    LoadingContent,
    LoadingMessage,
    StyledLoadingScreen,
} from "./styles";
import { MutatingDots } from "react-loader-spinner";
import { Bar } from "react-chartjs-2"; // Usar o Bar do react-chartjs-2
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement, // Registrar o BarElement
    Title,
    Tooltip,
    Legend,
} from "chart.js";

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement, // Registrar o BarElement
    Title,
    Tooltip,
    Legend
);

export default function Content() {
    const [cards, setCards] = useState([
        {
            title: "Previsão de inadimplência",
            description:
                "sit amet consectetur. Sit pretium bibendum sem vestibulum morbi quis odio. Magnis turpis in vitae risus habitant tempor metus placerat.",
            action: "Ver detalhes",
        },
        {
            title: "Previsão de inadimplência",
            description:
                "sit amet consectetur. Sit pretium bibendum sem vestibulum morbi quis odio. Magnis turpis in vitae risus habitant tempor metus placerat.",
            action: "Ver detalhes",
        },
        {
            title: "Previsão de inadimplência",
            description:
                "sit amet consectetur. Sit pretium bibendum sem vestibulum morbi quis odio. Magnis turpis in vitae risus habitant tempor metus placerat.",
            action: "Ver detalhes",
        },
        {
            title: "Previsão de inadimplência",
            description:
                "sit amet consectetur. Sit pretium bibendum sem vestibulum morbi quis odio. Magnis turpis in vitae risus habitant tempor metus placerat.",
            action: "Ver detalhes",
        },
    ]);
    const [visibleCards, setVisibleCards] = useState([]);
    const [sections, setSections] = useState([1, 2, 3, 4]);
    const [visibleSections, setVisibleSections] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const promise = axios.get(
            "http://localhost:8080/orquestrador/fetch_insights"
        );

        promise
            .then((response) => {
                setCards(response.data);
                setTimeout(() => {
                    setIsLoading(false);
                }, 3000);
            })
            .catch((error) => {
                console.log(error);
            });
    }, []);

    useEffect(() => {
        cards.forEach((card, index) => {
            setTimeout(() => {
                setVisibleCards((prev) => [...prev, index]);
            }, index * 700);
        });
    }, [cards]);

    useEffect(() => {
        sections.forEach((section, index) => {
            setTimeout(() => {
                setVisibleSections((prev) => [...prev, section]);
            }, index * 550);
        });
    }, [sections]);

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

    function getNextMonthDayMonth() {
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
        const dataProximoMes = new Date(dataAtual);
        dataProximoMes.setMonth(dataAtual.getMonth() + 1);
        const dia = dataProximoMes.getDate();
        const mes = meses[dataProximoMes.getMonth()];
        return `${dia} de ${mes}`;
    }

    const chartData = {
        labels: [
            "01/08",
            "02/08",
            "03/08",
            "04/08",
            "05/08",
            "06/08",
            "07/08",
            "08/08",
            "09/08",
            "10/08",
        ],
        datasets: [
            {
                label: "Receitas e Despesas",
                data: [10, 12, 15, 13, 18, 20, 25, 22, 27, 30],
                backgroundColor: "rgba(93, 99, 241, 0.6)",
                borderColor: "rgba(93, 99, 241, 0.4 )",
                borderWidth: 2,
            },
        ],
    };

    const options = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            x: { grid: { display: false } },
            y: { grid: { display: false }, beginAtZero: true },
        },
        plugins: {
            legend: { display: false },
        },
    };

    console.log({ isLoading });

    return (
        <>
            <Container>
                <GeneratedContent>
                    <Header>
                        <div>
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
                        </div>
                        <div>
                            <p>Ver todos</p>
                            <div>
                                <FaArrowRight />
                            </div>
                        </div>
                    </Header>
                    <Suggestions>
                        <div>
                            {cards.map((card, index) => (
                                <Suggestion
                                    key={index}
                                    visible={visibleCards.includes(index)}
                                >
                                    <h1>{card.title}</h1>
                                    <p>{card.description}</p>
                                    {card?.action ? (
                                        <div>
                                            <p>{card.action.type}</p>
                                            <div>
                                                <FaArrowRight />
                                            </div>
                                        </div>
                                    ) : (
                                        <></>
                                    )}
                                </Suggestion>
                            ))}
                        </div>
                    </Suggestions>
                </GeneratedContent>
                <AccountSummary>
                    <Profile isVisible={visibleSections.includes(1)}>
                        <h1>Peter Otto</h1>
                        <RiAccountCircleLine />
                    </Profile>
                    <Balance isVisible={visibleSections.includes(2)}>
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
                    <ChartData>
                        <Bar data={chartData} options={options} />
                    </ChartData>
                    <Predictions isVisible={visibleSections.includes(4)}>
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
                    <Predictions isVisible={visibleSections.includes(4)}>
                        <h1>
                            Previsões para daqui a 1 mês{" "}
                            <span>{getNextMonthDayMonth()}</span>
                        </h1>
                        <div>
                            <div>
                                <h2>Fechamento</h2>
                                <GrayBox>R$209.078</GrayBox>
                            </div>
                            <div>
                                <h2>Entradas</h2>
                                <GrayBox>R$159.078</GrayBox>
                            </div>
                            <div>
                                <h2>Saídas</h2>
                                <GrayBox>R$50.000</GrayBox>
                            </div>
                        </div>
                    </Predictions>
                </AccountSummary>
            </Container>

            {isLoading ? (
                <StyledLoadingScreen>
                    <LoadingContent>
                        <LoadingMessage>
                            Estamos gerando a sua interface personalizada...
                        </LoadingMessage>
                        <MutatingDots
                            visible={true}
                            height="100"
                            width="100"
                            color="#000"
                            secondaryColor="#000"
                            radius="12.5"
                            ariaLabel="mutating-dots-loading"
                            wrapperStyle={{}}
                            wrapperClass=""
                        />
                    </LoadingContent>
                </StyledLoadingScreen>
            ) : (
                <> </>
            )}
        </>
    );
}

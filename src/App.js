import React, { useEffect } from "react";
import './App.css';
import {
  Accordion, 
  AccordionSummary, 
  AccordionDetails, 
  Box, 
  Button, 
  Card, 
  Divider, 
  Grid, 
  TextField, 
  Typography, 
  Collapse,
  Dialog,
  DialogActions,
} from '@material-ui/core';

import { decode, listen, send_message, encode } from "./service/client_javascript";

function App() {
  const [sendMsgOpen, setSendMsgOpen] = React.useState(false);
  const [destiny, setDestiny] = React.useState("");
  const [user, setUser] = React.useState("");
  const [inputMsg, setInputMsg] = React.useState("");
  const [msgType, setMsgType] = React.useState("");
  const [graphOpen, setGraphOpen] = React.useState(false);
  const [sender, setSender] = React.useState("");
  const [incommingMsg, setIncommingMsg] = React.useState({});
  
  const [message, setMessage] = React.useState("");
  const [cryptedMsg, setCryptedMsg] = React.useState("");
  const [binaryMsg, setBinaryMsg] = React.useState("");
  const [encodedMsg, setEncondedMsg] = React.useState("");

  const handleUserChange = (event) => {
    setUser(event.target.value);
  }
  const handleDestinyChange = (event) => {
    setDestiny(event.target.value);
  }
  const handleInputMsgChange = (event) => {
    setInputMsg(event.target.value);
  }

  const handleSendMessage = () => {
    encode(inputMsg, setCryptedMsg, setBinaryMsg, setEncondedMsg);
    setMsgType("Send");
    setMessage(inputMsg);
  }

  const handleGraphClose = () => {
    setGraphOpen(false);
  };

  useEffect(() => {
    listen(user, setIncommingMsg)
    if (incommingMsg !== null && incommingMsg !== undefined && incommingMsg[0]) {
      setSender(incommingMsg.origin_name);
      setMessage(incommingMsg.message);
      setMsgType("received");
    }
  }, []);
  
  return (
    <div className="App">
      <header className="App-header">
        <React.Fragment>
          <Card style={{ padding: 40 }}>
            <Box style={{ maxWidth: "160vh" }}>
              <Grid container direction="row" alignItems="center" spacing={6}>
                <Grid item>
                  <Grid container direction="column" spacing={4}>
                    <Grid item>
                      <Typography color="primary" variant="h5" style={{ fontWeight: "bolder" }}>
                        A M I - P A G E R
                      </Typography>
                    </Grid>
                    <Grid item>
                      <Divider />
                    </Grid>
                    <Grid item>
                      <Grid container justifyContent="center" alignItems="center" spacing={6}>
                        <Grid item>
                          <TextField style={{ marginLeft: 4 }} value={user} onChange={handleUserChange} variant="standard" label="Digite seu nome"/>
                        </Grid>
                        <Grid item>
                          <TextField value={destiny} onChange={handleDestinyChange} variant="standard" label="Digite seu destinatário"/>
                        </Grid>{/*
                        <Grid item>
                          <Button variant="outlined">
                            Salvar
                          </Button>
                        </Grid>*/}
                      </Grid>
                    </Grid>
                    <Grid item>
                      <Grid container>
                        <TextField style={{ width: "78%"}} label="Digite sua mensagem" value={inputMsg} onChange={handleInputMsgChange} />
                        <Button variant="contained" style={{ marginLeft: 10}} disabled={user === "" || destiny === ""} onClick={handleSendMessage}>
                          Enviar
                        </Button>
                      </Grid>
                    </Grid>
                    <Grid item hidden={msgType === ""}>
                    <Collapse in={msgType !== ""}>
                      <Grid item>
                          <Card variant="outlined" style={{ maxWidth: "55vh",overflow: "auto" ,borderRadius: 0, padding: 5, borderWidth: 2, borderColor: msgType === "Send" ? "#ddd" : "#fff"}}>
                            <Typography variant="overline" color="#bbb">
                              {msgType === "Send" ? `Mensagem Enviada para ${destiny}` : "Mensagem Recebida"}
                            </Typography>
                            <Typography style={{ marginBottom: 15 }} >
                             {message}
                            </Typography>
                          </Card>
                      </Grid>
                      <Grid item>
                        <Button variant={sendMsgOpen ? "outlined" : "contained"} onClick={() => setSendMsgOpen(!sendMsgOpen)}>
                            Analisar Mensagem
                        </Button>
                        <Button style={{ marginLeft: 10 }} variant={graphOpen ? "outlined" : "contained"} onClick={() => setGraphOpen(true)}>
                            Gerar Gráfico
                        </Button>
                        <Dialog open={graphOpen}>
                          <DialogActions>
                            <Button onClick={handleGraphClose}>Fechar</Button>
                          </DialogActions>
                        </Dialog>
                      </Grid>
                    </Collapse>
                    </Grid>
                    <Grid item hidden={!sendMsgOpen}>
                      <Collapse in={sendMsgOpen}>
                        <Typography color="primary">
                          <Accordion>
                            <AccordionSummary>
                              <Typography>
                                Mensagem Criptografada
                              </Typography>
                            </AccordionSummary>
                            <AccordionDetails>
                              <Typography>{cryptedMsg}</Typography>
                            </AccordionDetails>
                          </Accordion>
                          <Accordion>
                            <AccordionSummary>
                              <Typography>
                                Mensagem em Binário
                              </Typography>
                            </AccordionSummary>
                            <AccordionDetails>
                              <Typography>{binaryMsg}</Typography>
                            </AccordionDetails>
                          </Accordion>
                          <Accordion>
                            <AccordionSummary>
                              <Typography>
                                Mensagem Codificada
                              </Typography>
                            </AccordionSummary>
                            <AccordionDetails>
                              <Typography>{encodedMsg}</Typography>
                            </AccordionDetails>
                          </Accordion>
                        </Typography>
                      </Collapse>
                    </Grid>
                  </Grid>
                </Grid>
              </Grid>
            </Box>
          </Card>
        </React.Fragment>
      </header>
    </div>
  );
}

export default App;

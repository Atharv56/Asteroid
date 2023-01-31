import React from "react";
import {Card, Form, Button, Container} from 'react-bootstrap'
export default function Predict() {
    return(
        <>
        <body className="bg-dark">
        <Container className="d-flex align-items-center justify-content-center" style={{minHeight: '100vh'}}>
        <div className='w-100' style={{maxWidth: '400px'}}>
        <Card className="bg-light">
            <Card.Body>
                <h2 className='text-center mb-4'>Prediction</h2>
                <Form>
                   <Form.Group id = 'text'>
                        <Form.Label>Enter the Magnitude</Form.Label>
                        <Form.Control></Form.Control>
                    </Form.Group> 
                    <Form.Group id = 'text'>
                        <Form.Label>Enter the Velocity</Form.Label>
                        <Form.Control></Form.Control>
                    </Form.Group> 
                    <Button type="button" className='w-100 mt-4 bg-success'>Predict</Button>
                </Form>
            </Card.Body>
            <Card.Body>
                <h2 className="text-center mb-4">Predicted diameter is</h2>
                <h5>{predict}</h5>
            </Card.Body>
        </Card>
        </div>
        </Container>
        </body>
        
        </>
    )
}
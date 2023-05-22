import React, { useState } from 'react';
import { Alert, Image } from 'react-native';
import {
    Container,
    Animation,
    Input,
    Button,
    ButtonText,
    AddressArea,
    Text
} from './styles';
import logo from '../../assets/logo.png';
import api from '../../services/api';

export default function Home() {
    const [cep, setCep] = useState('');
    const [address, setAddress] = useState(null);

    async function handleBuscar() {
        try {
            const { status, data } = await api.get(`${cep}/json/`);

            if (status != 200 || data.erro) {
                Alert.alert('Buscar', 'Digite um CEP válido.');
            } else {
                setAddress(data);
            }

        } catch (error) {
            Alert.alert('Buscar', 'Digite um CEP válido');
        }
    };

    async function handleLimpar() {
        setAddress(null);
        setCep('');
    }

    return (
        <Container>
            <Animation
                animation='bounceInDown'
                delay={100}
                duration={1500}
            >
                <Image source={logo} />
            </Animation>

            <Animation
                animation='bounceInRight'
                delay={100}
                duration={1500}
            >
                {!address &&
                    <Input
                        keyboardType="numeric"
                        maxLength={8}
                        onChangeText={setCep}
                        onSubmitEditing={handleBuscar}
                        placeholder="Digite o CEP que deseja buscar"
                        placeholderTextColor="#2F48D4"
                        value={cep}
                    />
                }

                <Button
                    activeOpacity={0.8}
                    onPress={address ? handleLimpar : handleBuscar}>
                    <ButtonText>
                        {address ? 'Limpar' : 'Buscar'}
                    </ButtonText>
                </Button>
            </Animation>

            {address &&
                <AddressArea>
                    <Text>CEP: {cep}</Text>
                    <Text>{address.logradouro}</Text>
                    <Text>Bairro: {address.bairro}</Text>
                    <Text>Cidade: {address.localidade}</Text>
                    <Text>IBGE: {address.ibge}</Text>
                    <Text>DDD: {address.ddd}</Text>
                    <Text>UF: {address.uf}</Text>
                </AddressArea>
            }
        </Container>
    );
}
import { useTranslation } from 'react-i18next';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import { motion } from 'framer-motion';
import PageWrapper from '../components/PageWrapper';

const About = () => {
  const { t } = useTranslation();

  return (
    <PageWrapper>
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
      >
        <Navbar />
        <section id="about">
          <h1>{t('about.title')}</h1>
          <p>{t('about.description')}</p>
        </section>
        <Footer />
      </motion.div>
    </PageWrapper>
  );
};

export default About;

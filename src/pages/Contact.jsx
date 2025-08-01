import { useTranslation } from 'react-i18next';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import { motion } from 'framer-motion';
import PageWrapper from '../components/PageWrapper';

const Contact = () => {
  const { t } = useTranslation();

  return (
    <PageWrapper>
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
      >
        <Navbar />
        <motion.section id="contact" initial={{ y: 20, opacity: 0 }} animate={{ y: 0, opacity: 1 }} transition={{ duration: 0.5 }}>
          <h1>{t('navbar.contact')}</h1>
          <p><a href="https://t.me/uzinex">{t('contact.telegram')}</a></p>
          <p><a href="https://threads.net/@uzinex_official">{t('contact.threads')}</a></p>
          <p>{t('contact.email')}: info@uzinex.uz</p>
        </motion.section>
        <Footer />
      </motion.div>
    </PageWrapper>
  );
};

export default Contact;
